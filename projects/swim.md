---
layout: work
type: Project
num: 10
worktitle: Simple Windowing Machine (SWIM)
---

## Overview

The Simple Windowing Machine (SWIM) is, as its name implies, a simple but 
functional operating system. It has the following features:

* Four distinct windows, each of which can run a program or edit a file.
  * An additional window displays the process manager.
* An interpreter for a simple programming language.
  * This will be provided for you to use.
* Dynamic memory allocation for user programs, with a copying garbage collector.
* A disk for persistent storage, simulated using a [RAM disk](https://hendrix-cs.github.io/csci320/projects/filesystem)

To begin this project, you need to have completed the preceding projects to at least Level 2:
* [Bare Metal Editor]({{site.baseurl}}/projects/bare_metal_editor.html)
* [Garbage Collection]({{site.baseurl}}/projects/garbage.html)
* [File System]({{site.baseurl}}/projects/filesystem.html)

## Setup
 
Use your repository for the [Bare Metal Editor]({{site.baseurl}}/projects/bare_metal_editor.html)
as the repository for this project. Add the following items to `Cargo.toml` under `[dependencies]`:
* `compiler_builtins = { version = "0.1", features = ["mem"] }` <!-- Fixed a bug - in the future, this goes in Project 7 -->
* `simple_interp = {git = "https://github.com/gjf2a/simple_interp"}`
* `gc_headers = {git = "https://github.com/gjf2a/gc_headers" }`
* `ramdisk = {git = "https://github.com/gjf2a/ramdisk"}`
* Link to the `GitHub` repository for your garbage collector. Use the format below, but 
  substitute your own repository name and URL:
  * `gc_heap = {git = "https://github.com/gjf2a/gc_heap" }`
* Link to the `GitHub` repository for your file system. Again, use the format below, but 
  substitute your own repository name and URL:
  * `file_system_solution = {git = "https://github.com/gjf2a/file_system_solution" }`
  
## Level 1: Incorporating the File System
* Add the following constants to `lib.rs`:
```
const TASK_MANAGER_WIDTH: usize = 10;
const WIN_REGION_WIDTH: usize = BUFFER_WIDTH - TASK_MANAGER_WIDTH;
const MAX_OPEN: usize = 16;
const BLOCK_SIZE: usize = 256;
const NUM_BLOCKS: usize = 255;
const MAX_FILE_BLOCKS: usize = 64;
const MAX_FILE_BYTES: usize = MAX_FILE_BLOCKS * BLOCK_SIZE;
const MAX_FILES_STORED: usize = 30;
const MAX_FILENAME_BYTES: usize = 10;
```
* Modify the following constant from the original template:
```
const WIN_WIDTH: usize = (WIN_REGION_WIDTH - 3) / 2;
```
* Add a `FileSystem` object to the `SwimInterface`.
* Use `open_create()`, `write()`, and `close()` at startup (i.e., in the `SwimInterface` 
`default()` method) to add the four files below to the file system:
  * **Note**: I highly recommend using Rust's [raw strings](https://stackoverflow.com/a/26621611) to encode these.
* Each file is listed in each of the four main windows. Each file listing is 
given in three columns, each of which may contain up to 10 rows.
* In each window, one of the files should be highlighted.
* If you use the left-arrow and right-arrow keys, it should cycle through the 
  files, highlighting the current file.

After completing Step 2, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_2.png" width=500> 

## File Text

### `hello` 
```
print("Hello, world!")
```

### `nums`
```
print(1)
print(257)
```

### `average`
```
sum := 0
count := 0
averaging := true
while averaging {
    num := input("Enter a number:")
    if (num == "quit") {
        averaging := false
    } else {
        sum := (sum + num)
        count := (count + 1)
    }
}
print((sum / count))
```
 
### `pi`
```
sum := 0
i := 0
neg := false
terms := input("Num terms:")
while (i < terms) {
    term := (1.0 / ((2.0 * i) + 1.0))
    if neg {
        term := -term
    }
    sum := (sum + term)
    neg := not neg
    i := (i + 1)
}
print((4 * sum))
```


## Level 2: Program Execution
* Add the following import to the top of `lib.rs`:
```
use simple_interp::{Interpreter, InterpreterOutput};
```
* When the user hits `r` when a file is highlighted, the file should **run**.
  * To run a program, create an `Interpreter` object for it using `Interpreter::new()`.
    The program text (as a `&str`) will be the parameter to `new()`. 
  * The `Interpreter` object's type
    will be `Interpreter<MAX_TOKENS, MAX_LITERAL_CHARS, STACK_DEPTH, MAX_LOCAL_VARS, WINDOW_WIDTH, CopyingHeap<HEAP_SIZE, MAX_HEAP_BLOCKS>>`
    The `Interpreter` type is defined in the [`simple_interp`](https://github.com/gjf2a/simple_interp) crate.
  * You will need to create a data type that implements the `InterpreterOutput`
    trait in order to receive output from the interpreter.
  * Use the `tick()` method to execute one instruction in the program.
    * If `tick()` returns `TickResult::AwaitInput`, block the process
      until input is available.
    * Once input is available, use the `provide_input()` method to send
      the input to the program.
* While the file is running, if the user hits `F6`, the program should immediately
  stop and return to the file selector.
* Ensure that all processes have a fair opportunity to run on the CPU.
* The number of instructions executed by each process should be shown in the 
  right window, as seen below:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_5.png" width=500>

## Level 3: File Editor

* If you type the `e` key, the highlighted file should be loaded into the editor. At this
point, we switch from file navigation to editing.
  * The selected filename appears as part of the window header, after the function 
    key.
  * SWIM opens the file and reads its contents so as to be visible. It then closes
    the file.
  * As with the filename editing, each keystroke appears in the appropriate window,
    with the backspace operating properly as well.
  * Entering `F6` uses `open_create()` to reopen the file. It writes the contents 
    of the editor's buffer to disk, then closes the file, restoring the window to 
    the file selection screen.
  * When the file is re-opened, from any of the windows, the changes saved earlier
    should be reflected.
* When `F5` is selected, the user can enter a filename of up to 10 characters
  in the top window.
  * When the user types the backspace (Unicode ``\u{8}``), it erases the previous 
    character.
  * When the user types the Enter key:
    * An empty file with the given name is opened, created, and closed on the disk
    * The filename is cleared from the top window
    * The file listings in the four quadrant windows are updated to include the new file
    
When creating a file named `test`, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3a.png" width=500>

When navigating to edit the file `test` in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3b.png" width=500>

While editing the file in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3c.png" width=500>

After saving the file using `F6` and reopening it in the `F2` buffer, it should look
like this:
<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3d.png" width=500>    


## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).
