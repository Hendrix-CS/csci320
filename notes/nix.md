---
layout: work
worktitle: `nix` crate notes
---

The [`nix`](https://crates.io/crates/nix) crate for Rust provides a Rust-friendly API for 
Unix system calls. But it is not always clear how to invoke the `nix` system calls. 
Consider the following example from the [Files and Directories chapter]() of [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/):

```
int fd = open("foo", O_CREAT | O_WRONLY | O_TRUNC, S_IRUSR | S_IWUSR);
```

A translation into Rust using `nix` could look like this:
```
let flags: OFlag = [OFlag::O_CREAT, OFlag::O_WRONLY, OFlag::O_TRUNC].iter().copied().collect();
let mode: Mode = [Mode::S_IRUSR, Mode::S_IWUSR].iter().copied().collect();
let fd = open("foo", flags, mode)?;
```

The [`OFlag`](https://docs.rs/nix/0.26.2/nix/fcntl/struct.OFlag.html) data type represents
bit configuration flags. The parameter to the actual system call is an integer whose 
individual bits represent different requests. In the C language API, we use bitwise OR
to combine those bits. In Rust, using `collect()` on the various constants performs an
implicit bitwise OR to combine them.

Having created a file, we next would want to write to it:

```
let text = "Hello, world!";
let written = write(fd, text.as_bytes())?;
close(fd)?;
println!("Wrote {written} bytes to file descriptor {fd}");
```

The above is very similar to what one would write in C. The main 
difference is the need to convert the string to an array of bytes,
performed by `as_bytes()`. 

To read from a file:
```
fn dump(filename: &str) -> anyhow::Result<()> {
    let fd = open(filename, OFlag::O_RDONLY, Mode::empty())?;
    println!("Opening {filename} with file descriptor {fd}");
    let mut bytes = [0; 100];
    let mut bytes_read = bytes.len();
    while bytes_read == bytes.len() {
        bytes_read = read(fd, &mut bytes)?;
        for i in bytes_read..bytes.len() {
            bytes[i] = 0;
        }
        print!("{}", std::str::from_utf8(&bytes)?);
    }
    println!();
    close(fd)?;
    Ok(())
}
```
------------------------------------------------------------------------
