---
layout: work
type: Project
num: 10
worktitle: Simple Windowing Machine
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

## Step 1: Windows

Using the provided template code, write a bare-metal program to support a 
windowing environment as follows:
* Divide the VGA buffer into the following areas:
  * The rightmost 10 columns are reserved for process management.
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
  * [Tell them the other constant stats to use]
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
done := false
while not done {
    num := input("Enter a number:")
    if num == "quit" {
        done := true
    } else {
        sum := sum + num
        count := count + 1
    }
}
print(sum / count)
```
  * `pi`
```
sum := 0
i := 0
neg := false
terms := input("Num terms:")
while i < terms {
    term := 1 / ((2 * i) + 1)
    if neg {
        term := -term
    }
    sum := sum + term
    neg := not neg
    i := i + 1
}
print(4 * sum)
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

## Step 4: A Copying Garbage Collector

## Step 5: Creating and Managing Processes

## Submissions
* Create a **private** GitHub repository for your SWIM kernel.
* Paste the repository URL into your Teams channel.

## Assessment
* **Partial**: Completes Step 1 and either Step 2 or Step 4.
* **Complete**: Meets all requirements given above.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).
