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
  * `hello` 
```
print("Hello, world!")
```

  * `nums`
```
print(1)
print(257)
```
  * `average`
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
  * `pi`
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
* Each file is listed in each of the four main windows. Each file listing is 
given in three columns, each of which may contain up to 10 rows.
* In each window, one of the files should be highlighted.
* If you use the left-arrow and right-arrow keys, it should cycle through the 
  files, highlighting the current file.

After completing Step 2, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_2.png" width=500> 

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

<!-- Level 3 -->
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
    
when creating a file named `test`, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3a.png" width=500>

When navigating to edit the file `test` in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3b.png" width=500>

While editing the file in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3c.png" width=500>

After saving the file using `F6` and reopening it in the `F2` buffer, it should look
like this:
<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3d.png" width=500>    

<!-- Original
## Overview

The Simple Windowing Machine (SWIM) is, as its name implies, a simple but 
functional operating system. It has the following features:

* Four distinct windows, each of which can run a program or edit a file.
  * An additional window displays the process manager.
* An interpreter for a simple programming language.
  * This will be provided for you to use.
* Dynamic memory allocation for user programs, with a copying garbage collector.
* A disk for persistent storage, simulated using a [RAM disk](https://hendrix-cs.github.io/csci320/projects/filesystem)

## Step 1: Windows

Using the [provided template code](https://github.com/gjf2a/swim_template), 
write a bare-metal program to support a windowing environment as follows:
* Divide the VGA buffer into the following areas:
  * The rightmost 10 columns are reserved for process status information.
  * Row 0 is reserved for entering filenames.
  * The remaining area is divided into four equal-sized quadrants.
* The window boundaries are drawn using `.` characters.
  * Row 1 is the top boundary.
  * The currently selected window has its boundaries drawn with `*` characters.
* Function keys `F1`, `F2`, `F3`, and `F4` are used to select the current window.
  * When a window is selected, its boundary characters change immediately.
  * At the midpoint of each window header, include the function key code for 
    selecting that window.
* Function key `F5` is used to select the filename-entry row. None of the windows
  are highlighted when this row is active.
* If the file exceeds the buffer size, `F7` scrolls up one line, and `F8` scrolls 
  down one line.

After completing Step 1, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_1.png" width=500>

## Step 2: Incorporating the File System
* Add the method `pub fn list_directory(&mut self) -> FileSystemResult<(usize, [[u8; MAX_FILENAME_BYTES]; MAX_FILES_STORED])>` to `struct FileSystem` 
  * It will return the total number of files stored, as well as the bytes in the 
    filename of each file.
* Add a link to your GitHub repository for your 
  [Project 9 solution](https://hendrix-cs.github.io/csci320/projects/filesystem)
  in your `Cargo.toml` file. For example, here is what that line looks like in my
  own `Cargo.toml`: `file_system_solution = {git = "https://github.com/gjf2a/file_system_solution"}`
* Add a `FileSystem` object to your kernel, using the following constants:
  * `const MAX_OPEN: usize = 16;`
  * `const BLOCK_SIZE: usize = 256;`
  * `const NUM_BLOCKS: usize = 255;`
  * `const MAX_FILE_BLOCKS: usize = 64;`
  * `const MAX_FILE_BYTES: usize = MAX_FILE_BLOCKS * BLOCK_SIZE;`
  * `const MAX_FILES_STORED: usize = 30;`
  * `const MAX_FILENAME_BYTES: usize = 10;`
* When you add your `FileSystem` object, create four files and store them, so that
  it has some contents when the OS starts up. Here are four files for you to use:
  * `hello` 
```
print("Hello, world!")
```

  * `nums`
```
print(1)
print(257)
```
  * `average`
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
  * `pi`
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
* Each file is listed in each of the four main windows. Each file listing is 
given in three columns, each of which may contain up to 10 rows.

After completing Step 2, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_2.png" width=500>

## Step 3: Selecting and Editing Files
* When `F5` is selected, the user can enter a filename of up to 10 characters
  in the top window.
  * When the user types the backspace (Unicode ``\u{8}``), it erases the previous 
    character.
  * When the user types the Enter key:
    * An empty file with the given name is opened, created, and closed on the disk
    * The filename is cleared from the top window
    * The file listings in the four quadrant windows are updated to include the new file
* When the user hits one of the other function keys, it switches to the
  designated buffer. Within the buffer, the arrow keys are used to navigate among 
  the columns. Exactly one filename is always highlighted within the selected
  window.
* When the user hits the `e` key, the selected window switches into Editor mode:
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

After completing Step 3, when creating a file named `test`, SWIM should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3a.png" width=500>

When navigating to edit the file `test` in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3b.png" width=500>

While editing the file in the `F1` buffer, it should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3c.png" width=500>

After saving the file using `F6` and reopening it in the `F2` buffer, it should look
like this:
<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_step_3d.png" width=500>

## Step 4: A Copying Garbage Collector
* Implement a copying garbage collector.
* Use [this template](https://github.com/gjf2a/gc_heap_template) for building 
  your solution. 
* Also examine the [gc_headers](https://github.com/gjf2a/gc_headers)
  to familiarize yourself with the data structures you will be using.
  * `Pointer` objects are the means by which entities using the heap
  refer to memory. 
  * Each `Pointer` object includes:
    * A block number that uniquely identifies the allocated block.
    * An offset into that block, to access a specific memory location.
    * The total size of the block.
  * The malloc() method will perform an allocation, returning a `Pointer`
  to the newly allocated memory. The `Pointer` will include a unique block
  number for the allocation, along with its size. The `offset` will be zero, 
  referencing the first memory location in the block.
  * The `load()` and `store()` methods in conjunction with `Pointer`s are 
  used to retrieve and update values in heap-allocated RAM.
  * Entities using the heap only use `Pointer` objects - they are never
  given access to the specific memory address of the memory they are using.
    * This is because the garbage collector might relocate memory to a
      new address when collecting. 
    * By referencing memory exclusively through block numbers, the 
      relocation process is made invisible to the user.
* When `malloc()` is called but there is no more space in the heap,
  the collector will call the `trace()` method of its `Tracer` parameter
  to find out which blocks are in use.
  * The collector should provide an array of `MAX_BLOCKS` boolean values
    to `trace()`. All of the values in the array should initially be `false`.
  * The `Tracer` will mark `true` for each block it wants to keep.
  * The collector will then copy each `true` block to the new heap, 
    updating their addresses as they are moved.

## Step 5: Creating and Managing Processes
* When the user hits `r` when a file is highlighted, the file should **run**.
  * To run a program, create an `Interpreter` object for it using `Interpreter::new()`.
    The program text (as a `&str`) will be the parameter to `new()`. 
  * The `Interpreter` object's type
    will be `Interpreter<MAX_TOKENS, MAX_LITERAL_CHARS, STACK_DEPTH, MAX_LOCAL_VARS, WINDOW_WIDTH, CopyingHeap<HEAP_SIZE, MAX_HEAP_BLOCKS>>`
    The `Interpreter` type is defined in the [`simple_interp`](https://github.com/gjf2a/simple_interp) crate; a reference to it is included in the `Cargo.toml`
    file in the template.
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


## Submissions
* Create a **private** GitHub repository for your SWIM kernel.
* Paste the repository URL into your Teams channel.

## Assessment
* **Partial**: Completes Step 1 and either Step 2 or Step 4.
* **Complete**: Meets all requirements given above. Never panics!
-->

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).
