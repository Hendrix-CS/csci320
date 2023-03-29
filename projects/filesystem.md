---
layout: work
type: Project
num: 9
worktitle: File System
---

Persistent data is stored in hardware media such as hard drives and flash RAM. From
the perspective of the operating system, both types of hardware are accessed by
two instructions:
* Read data from a block
* Write data to a block

The job of the file system is to organize disk blocks into files and directories
so that users can store and retrieve persistent data in an intuitive way.

In this assignment, we will simulate persistent storage using a 
[**RAM Disk**](https://github.com/gjf2a/ramdisk). The RAM disk will present
the above interface, although the data it stores will only persist as long as 
our file system program is executing.  

## A Very Simple File System

Our file system will have the following capabilities:
* Create a new file.
* Open a file for reading.
* Open an existing file to append.
* Read from a file open for reading.
* Write to a newly created file or file open for appending.
* Close a file.
* All files will be stored in a single root directory. There is no directory 
  hierarchy.
* As part of the OS, it will, of course, have to be able to run on bare metal 
  (`no-std`).

The file system is constrained by a number of constants:
* `MAX_OPEN`: Maximum number of open files.
* `BLOCK_SIZE`: Number of bytes in a disk block.
* `NUM_BLOCKS`: Total disk blocks.
  * It must be representable as an 8-bit value.
  * The total storage capacity of the disk is `NUM_BLOCKS * BLOCK_SIZE`.
* `MAX_FILE_BLOCKS`: Maximum number of blocks for a single file.
  * Each inode requires 2 + `MAX_FILE_BLOCKS` bytes
* `MAX_FILE_BYTES`: Maximum number of bytes in a single file.
  * `MAX_FILE_BYTES = MAX_FILE_BLOCKS * BLOCK_SIZE`
  * It must be representable as a 16-bit value.
* `MAX_FILES_STORED`: Maximum number of files that the file system can track.
  * The number of inode blocks is `MAX_FILES_STORED /` the size of an inode. 
* `MAX_FILENAME_BYTES`: Maximum number of characters in a filename.

Some of these constants are intrinsic to a file system. Others are introduced
to simplify our implementation.

## Data Structures

The file system blocks are laid out as follows:
* Block 0: Each bit indicates whether an inode block is in use or not.
* Block 1: Each bit indicates whether a data block is in use or not.
* Blocks 2 through 1 + number of inode blocks: Inode table
* Blocks 2 + number of inode blocks up to `NUM_BLOCKS`: Data blocks.

Each inode consists of:
* A 16-bit value representing total bytes stored in the file.
* An array of each block in active use. Each block number is represented as a 
  single byte.
* The directory file is stored in inode 0.

The file system data structure itself consists of:
* An array of open files.
* The RAM disk.
* Any buffers you would like to use. Buffers for both single blocks and entire
  files may be useful.

Each open file is represented by:
* Its inode number.
* Its inode.
* Whether it is opened for reading or writing.
* The current block being read/written.
* The next byte in the block to be read/written.

## Algorithms

To create a file:
* Create the directory file, if it does not already exist.
* Select an inode number.
* Select a data block number for the first block.
* Create an inode for the new file, and save it in the inode table.
* Update the directory file with an entry for the new file.
* Create a file table entry for the newly created file, and return the file 
  descriptor.

To open a file to read:
* Load the directory file, and find the file's inode.
* Create a file table entry for the newly opened file, and return the file 
  descriptor.

To open a file to append:
* Load the directory file, and find the file's inode.
* Create a file table entry for the newly opened file, and return the file
  descriptor. The current block and offset should point at the **end** of the file.

To read from a file:
* The user will provide a buffer to store the incoming data.
* Copy bytes from the file into the buffer until the buffer is full.
* Update the current block and offset appropriately.

To write to a file:
* The user will provide data to be written in a buffer.
* Copy all bytes from the user's buffer.
* Update the current block and offset appropriately.

To close a file:
* If the file was open for writing, update its inode to store its new size.
  
## Code skeleton

Add `ramdisk = {git = "https://github.com/gjf2a/ramdisk"}` as a dependency in
`Cargo.toml`.

Use the following code as a starting point for your program:
```
#![cfg_attr(not(test), no_std)]

#[derive(Copy, Clone, PartialEq, Eq)]
pub enum FileSystemResult<T: Copy + Clone> {
    Ok(T),
    Err(FileSystemError),
}

impl<T: Copy + Clone> FileSystemResult<T> {
    pub fn unwrap(&self) -> T {
        match self {
            FileSystemResult::Ok(v) => *v,
            FileSystemResult::Err(e) => panic!("Error: {e:?}"),
        }
    }
}

#[derive(Copy, Clone, Eq, PartialEq, Debug)]
pub enum FileSystemError {
    FileNotFound,
    FileNotOpen,
    NotOpenForRead,
    NotOpenForWrite,
    TooManyOpen,
    TooManyFiles,
    AlreadyOpen,
    DiskFull,
    FileTooBig,
    FilenameTooLong,
    InvalidFileDescriptor(usize),
}

#[derive(Debug, Copy, Clone)]
pub struct FileInfo<const MAX_BLOCKS: usize, const BLOCK_SIZE: usize> {
    inode: Inode<MAX_BLOCKS, BLOCK_SIZE>,
    inode_num: usize,
    current_block: usize,
    offset: usize,
    writing: bool,
}

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub struct Inode<const MAX_BLOCKS: usize, const BLOCK_SIZE: usize> {
    bytes_stored: u16,
    blocks: [u8; MAX_BLOCKS],
}

const INODE_FULL_BLOCK: usize = 0;
const DATA_FULL_BLOCK: usize = INODE_FULL_BLOCK + 1;
const INODE_TABLE_START: usize = DATA_FULL_BLOCK + 1;

#[derive(core::fmt::Debug)]
pub struct FileSystem<
    const MAX_OPEN: usize,
    const BLOCK_SIZE: usize,
    const NUM_BLOCKS: usize,
    const MAX_FILE_BLOCKS: usize,
    const MAX_FILE_BYTES: usize,
    const MAX_FILES_STORED: usize,
    const MAX_FILENAME_BYTES: usize,
> {
    open: [Option<FileInfo<MAX_FILE_BLOCKS, BLOCK_SIZE>>; MAX_OPEN],
    disk: ramdisk::RamDisk<BLOCK_SIZE, NUM_BLOCKS>,
    block_buffer: [u8; BLOCK_SIZE],
    file_content_buffer: [u8; MAX_FILE_BYTES],
}

impl<
        const MAX_OPEN: usize,
        const BLOCK_SIZE: usize,
        const NUM_BLOCKS: usize,
        const MAX_FILE_BLOCKS: usize,
        const MAX_FILE_BYTES: usize,
        const MAX_FILES_STORED: usize,
        const MAX_FILENAME_BYTES: usize,
    >
    FileSystem<
        MAX_OPEN,
        BLOCK_SIZE,
        NUM_BLOCKS,
        MAX_FILE_BLOCKS,
        MAX_FILE_BYTES,
        MAX_FILES_STORED,
        MAX_FILENAME_BYTES,
    >
{
    pub fn new(disk: ramdisk::RamDisk<BLOCK_SIZE, NUM_BLOCKS>) -> Self {
        assert_eq!(MAX_FILE_BYTES, MAX_FILE_BLOCKS * BLOCK_SIZE);
        assert!(NUM_BLOCKS <= u8::MAX as usize);
        assert!(MAX_FILE_BYTES <= u16::MAX as usize);
        let block_bits = BLOCK_SIZE * 8;
        assert!(MAX_FILES_STORED <= block_bits);
        assert!(MAX_FILES_STORED <= u16::MAX as usize);
        let result = Self {
            open: [None; MAX_OPEN],
            disk,
            block_buffer: [0; BLOCK_SIZE],
            file_content_buffer: [0; MAX_FILE_BYTES],
        };
        assert!(result.num_inode_blocks() * 2 < NUM_BLOCKS);
        assert!(result.num_data_blocks() <= block_bits);
        assert_eq!(
            result.num_data_blocks() + result.num_inode_blocks() + 2,
            NUM_BLOCKS
        );
        assert!(result.num_inode_entries() <= u16::MAX as usize);
        assert!(result.num_inode_blocks() <= MAX_FILE_BLOCKS);
        result
    }

    pub fn max_file_size(&self) -> usize {
        MAX_FILE_BLOCKS * BLOCK_SIZE
    }

    pub fn num_inode_bytes(&self) -> usize {
        2 + MAX_FILE_BLOCKS
    }

    pub fn inodes_per_block(&self) -> usize {
        BLOCK_SIZE / self.num_inode_bytes()
    }

    pub fn num_inode_blocks(&self) -> usize {
        MAX_FILES_STORED / self.inodes_per_block()
    }

    pub fn num_data_blocks(&self) -> usize {
        NUM_BLOCKS - self.num_inode_blocks() - 2
    }

    pub fn num_inode_entries(&self) -> usize {
        self.inodes_per_block() * self.num_inode_blocks() * self.num_inode_bytes()
    }

    pub fn first_data_block(&self) -> usize {
        2 + self.num_inode_blocks()
    }

    pub fn open_read(&mut self, filename: &str) -> FileSystemResult<usize> {
        todo!("Your code here");
    }

    pub fn open_create(&mut self, filename: &str) -> FileSystemResult<usize> {
        todo!("Your code here");
    }

    pub fn open_append(&mut self, filename: &str) -> FileSystemResult<usize> {
        todo!("Your code here");
    }

    pub fn close(&mut self, fd: usize) -> FileSystemResult<()> {
        todo!("Your code here");
    }

    pub fn read(&mut self, fd: usize, buffer: &mut [u8]) -> FileSystemResult<usize> {
        todo!("Your code here");
    }

    pub fn write(&mut self, fd: usize, buffer: &[u8]) -> FileSystemResult<()> {
        todo!("Your code here");
    }
}
```

Here are some sample unit tests. For this assignment, you will be running the file
system **entirely through unit tests**. Part of the assignment is to write unit
tests sufficient to demonstrate that it works.

```

#[cfg(test)]
mod tests {
    use super::*;

    fn make_small_fs() -> FileSystem<16, 64, 255, 8, 512, 32, 8> {
        FileSystem::new(ramdisk::RamDisk::new())
    }

    #[test]
    fn test_empty() {
        let mut sys = make_small_fs();
        assert!(!sys.directory_exists());
        assert!(sys.inode_for("test") == FileSystemResult::Err(FileSystemError::FileNotFound));
    }

    #[test]
    fn test_short_write() {
        let mut sys = make_small_fs();
        let f1 = sys.open_create("one.txt").unwrap();
        sys.write(f1, "This is a test.".as_bytes()).unwrap();
        let mut buffer = [0; 50];
        sys.close(f1).unwrap();
        let f2 = sys.open_read("one.txt").unwrap();
        let bytes_read = sys.read(f2, &mut buffer).unwrap();
        assert_eq!(bytes_read, 15);
        let s = core::str::from_utf8(&buffer[0..bytes_read]).unwrap();
        assert_eq!(s, "This is a test.");
    }
}

```

## Submissions
Create a **private** GitHub project entitled `file_system`, and add the instructor
as a collaborator.


## Assessment
* **Partial**: 
  * File creation, reading, writing, and closing are all implemented.
  * Unit tests suffice to demonstate their correctness.
* **Complete**: 
  * Open for appending is implemented, and correctness demonstrated.
  * All error conditions are handled without panics.

------------------------------------------------------------------------
