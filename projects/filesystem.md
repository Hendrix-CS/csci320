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

Fork the [File System Template](https://github.com/gjf2a/file_system_template) repository to create your solution for this assignment.

We will compile and run this project entirely through Rust's unit-testing mechanism. Run `cargo test` to run the unit tests.

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
  * In the unit tests below, this value is stored in a little-Endian format;
    that is, the first byte represents the low-order bits, and the 
    second byte represents the high-order bits. 
  * For example, the number 300 requires 9 bits to represent it in binary: `100101100`
    * The bits `00101100` are the low-order bits, and are represented
      with the decimal value `44` in the first byte.
    * The bits `00000001` are the high-order bits, and are represented
      with the decimal value `1` in the second byte.
* An array of each block in active use. Each block number is represented as a 
  single byte.
* The directory file is stored in inode 0.

The file system data structure itself consists of:
* An array of open files.
* The RAM disk.
* An array of boolean values, indicating whether the inode of that index is open.
* A buffer of the same size as a disk block.
* A buffer of the same size as an entire file.

Each open file is represented by:
* Its inode number.
* Its inode.
* Whether it is opened for reading or writing.
* The current block being read/written.
* The next byte in the block to be read/written.

## Algorithms

To create a file:
* Create the directory file, if it does not already exist.
  * To check if it exists, see if inode 0 is in use.
  * If it does not exist:
    * Set the bit for inode 0 to 1.
    * Select its first data block.
    * Create an inode for the directory, and save it in the inode table.
* Search the directory file for the filename
  * If the file already has an inode: **(Optional; Level 3)**
    * Use the current inode.
    * Reset its stored-bytes and current-block to a state as if it were
      newly created.
    * Clear the in-use bits for its existing data blocks, except for the
      first data block. We will continue to use that block as we start
      the write.
  * Otherwise:
    * Select an inode number.
    * Select a data block number for the first block.
    * Create an inode for the new file, and save it in the inode table.
    * Update the directory file with an entry for the new file.
* Create a file table entry for the newly created file, and return the file 
  descriptor.

To open a file to read:
* Load the directory file, and find the file's inode.
  * If the file is not present in the directory, return an error.
  * If the inode is already open, return an error.
* Create a file table entry (a `FileInfo` object) for the newly opened file.
* Read in the first block of the newly opened file into the file table
  entry's buffer.
* Mark the inode as open in `open_inodes`
* Return the file descriptor, that is, the index of the file table 
  used for its `FileInfo`.

To open a file to append: **(Optional; Level 3)**
* Load the directory file, and find the file's inode.
  * If the file is not present in the directory, return an error.
  * If the inode is already open, return an error.
* Create a file table entry for the newly opened file
  * The current block and offset should point at the **end** of the file.
  * Read the current block into the file table entry's buffer.
* Return the file descriptor. 

To read from a file:
* The user will provide a buffer to store the incoming data.
* Copy bytes from the file into the buffer until the buffer is full
  or there is no more data in the file.
  * If you exhaust the current block, update the current block and offset,
    then read the next block from the disk into the buffer.

To write to a file:
* The user will provide data to be written in a buffer.
* Copy all bytes from the user's buffer into the block buffer.
  * If you fill the block buffer:
    * Write its contents to the disk.
    * Update the current block and offset appropriately.

To close a file:
* If the file was open for writing, update its inode to store its new size.
* Remove the entry in the file table.
* Mark the inode as closed in `open_inodes`.

## Error Conditions
Return each of the conditions below if...
* `FileNotFound`
  * ...a filename is not present in the directory
* `FileNotOpen`
  * ...the given file descriptor corresponds to a `None` value in the `open` table.
* `NotOpenForRead`
  * ...the `writing` flag is `true` for the given file descriptor and
    the user attempts a `read()`.
* `NotOpenForWrite`
  * ...the `writing` flag is `false` for the given file descriptor and
    the user attempts a `write()`.
* `TooManyOpen`
  * ...every entry in `open` is `Some(...)`, and an attempt is made to open
    another file.
* `TooManyFiles`
  * ...every available inode table entry is claimed in block 0, and `open_create()` is called.
* `AlreadyOpen`
  * ...the given inode already corresponds to an open file. 
  * The `open_inodes` array is useful for detecting this.
* `DiskFull`
  * ...a new block is requested for a file, but every available data black
    is already claimed in block 1.
* `FileTooBig`
  * ...a new block is requested for a file, but it already uses the 
    maximum allowed blocks for a single file.
* `FilenameTooLong`
  * ...a new file is created in `open_create()`, but the filename exceeds
    the maximum allowed number of characters.

## Debugging
Since the file system code is set up to run as `no-std`, you can't normally
use `println!()` to help debug it. However, as a temporary measure, you
can re-enable the standard library for debugging purposes.

The key line for compiling as `no-std` is at the top of the program:
```
#![cfg_attr(not(test), no_std)]
```

If you want to use `println!()` to help debug, comment that line out:
```
//#![cfg_attr(not(test), no_std)]
```

Once you have gotten the information you need, be sure to restore the line!

Related to this, you can print the ramdisk itself:
* `println!("{:?}", self.disk);` should display the disk contents.

## Submissions
Add the instructor as a collaborator on your **private** fork of the repository.

## Assessment
* Level 1:
  * Passes the following unit tests.
    * `test_no_directory_exists()`
    * `test_directory_exists()`
    * `test_load_file_bytes()`
    * `test_save_file_bytes()`
    * `test_activate_bit()`
    * `test_request_data_block()`
    * `test_clear_block_buffer()`
    * `test_inode_table_inode()`
    * `test_update_inode_table()`
    * `test_inode_from_bytes()`
    * `test_save_inode()`
    * `test_load_inode()`
    * `test_mark_inode_blocks_in_use()`
    * `test_initialize_new_file_1()`
    * `test_initialize_new_file_2()`
    * `test_directory_inode_1()`
    * `test_directory_inode_2()`
    * `test_load_directory()`
    * `test_list_directory_fail()`
    * `test_list_directory_succeed()`
    * `test_inode_for()`
* Level 2:
  * Passes all of the unit tests above.
  * Also passes the following unit tests:
    * `test_empty()`
    * `test_short_write()`
    * `test_long_write()`
    * `test_complex_1()`
* Level 3:
  * Passes all of the unit tests above.
  * Also passes the following unit tests:
    * `test_complex_2()`
    * `test_complex_3()`
    * `test_file_not_found()`
    * `test_file_not_open()`
    * `test_not_open_for_read()`
    * `test_not_open_for_write()`
    * `test_filename_too_long()`
    * `test_already_open()`
    * `test_file_too_big()`
    * `test_too_many_files()`
    * `test_disk_full()`

------------------------------------------------------------------------
