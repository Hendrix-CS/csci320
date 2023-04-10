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
  * `hello`: `print("Hello, world!")`
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
    * An empty file is created on the disk with the given name, 
    * The filename is cleared from the top window
    * The file listings in the four quadrant windows are updated to include the new file
* When the user hits one of the other function keys, it switches to the
  designated buffer. Within the buffer, the arrow keys are used to navigate among 
  the columns. Exactly one filename is always highlighted within the selected
  window.
* When the user hits the `e` key, the selected window switches into Editor mode:
  * The selected filename appears as part of the window header, after the function 
    key.
  * As with the filename editing, each keystroke appears in the appropriate window,
    with the backspace operating properly as well.
  * Entering `F6` saves and closes the file, restoring the window to the file 
    selection screen.
  * If a file is already open in a different window, trying to edit it will have
    no effect.
  * When the file is re-opened, from any of the windows, the changes saved earlier
    should be reflected.

After completing Step 3, SWIM should look like this:

################################

## Overview

In a cooperative multitasking environment, each concurrent task voluntarily yields
control to the CPU at certain prearranged times. A kernel with cooperative 
multitasking is significantly easier to implement than one with preemptive 
multitasking, so our focus for this project will be to assume cooperative 
multitasking.

This is a **complex project**. Please clone the 
[`coop_os_starter`](https://github.com/gjf2a/coop_os_starter)
repository to use as a starting point for your implementation.

## The Cooperative Multitasking Kernel

Each task that is run by our kernel is a **state machine**. At each time step,
each state machine can perform one of the following actions:
* Request keyboard input
* Request that output be printed to the screen
* Perform one step of its algorithm

The kernel runs up to four tasks. Each task has its own subwindow for input and
output. In the background, the kernel runs the following algorithm:

	loop indefinitely
		Ask the scheduler which process to run
		Run one instruction for the selected process
		
The effect of running an instruction depends upon its type:
* Input instruction: 
  * Process blocks, awaiting input
* Output instruction: 
  * Kernel outputs data from process
* Update instruction: 
  * Kernel instructs process to update itself by one computation step
  * Process yields control back to the kernel after completing this step
    * This is the "cooperative" aspect of the kernel
  
When a keyboard interrupt occurs:
* `F1`, `F2`, `F3`, `F4`: Switch to the appropriate process/window
  * Note that the window border of the selected process is outlined in `*`
    characters rather than `.` characters.
* If no program is running in the current window:
  * `ArrowUp`, `ArrowDown`: Switch between candidate programs to run
  * `Enter`: Start the currently selected program
* All others:
  * Store the key in a buffer for the current process
  * If a newline, send the string in the buffer to the process, and clear the buffer
  
When a timer interrupt occurs:
* Process status side window is updated
  * For each process, it displays the total number of updates since
    it started running
	
Here is a screenshot of how the Cooperative Multitasking Kernel looks:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/coop_os_four_procs.png" width=500>

In this screenshot:
* Process `F1` has completed. Its result is displayed, and the user can select to run
  a new process in that space.
* Processes `F2` and `F3` are in progress.
* Process `F4` is blocked awaiting user input.

## State Machine Processes

Each process state machine implements the following trait:

	pub trait StateMachine {
		fn next_instruction(&mut self) -> Option<Instruction>;
		fn update(&mut self);
		fn receive_input(&mut self, value: &str) -> Option<&'static str>;
	}
	
* The `next_instruction()` method requests the next instruction that the 
process would like to execute. 
* The `update()` method is called to ask the process to update itself by one step,
then cooperatively yield control of the CPU.
* The `receive_input()` method is called in order to relay keyboard input
to the process.

Here are the possible values for an `Instruction`:

	#[derive(Copy,Clone)]
	pub enum Instruction {
		PrintStr(&'static str),
		PrintInt(isize),
		PrintFloat(f64),
		Input(&'static str),
		Update
	}
	
When the kernel calls `next_instruction()`:
* If it receives one of the `Print` instructions, it should print the supplied
value into the appropriate process window.
* If it receives the `Update` instruction, it should call the `update()` method.
* If it receives the `Input` instruction, it should print the supplied string
and block the process until it receives a line of input.

The [iter_state_machine](https://github.com/gjf2a/iter_state_machine) crate 
includes two implementations of this trait:
* `Average`: Requests a sequence of integers from the user. Upon entering 
a negative number, it prints their average.
* `Pi`: Requests a tolerance level from the user, after which it uses the 
power series to compute the value within that tolerance.

These are the two different process types you will implement in this assignment.

## Scheduling

In the [provided code](https://github.com/gjf2a/coop_os_starter) is a 
`Policy` type. This `enum` represents possible alternative scheduling policies.
The only policy currently implemented is to run the current process to 
completion. Add `enum` alternatives for the following policies:
* From [Scheduling: Introduction](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf): Round Robin
* [Multi-Level Feedback Queue](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf)
  
Try out your kernel with your different schedulers. How do they perform?
Do they work as advertised? Feel free to add additional information to 
`draw_proc_status()` to help with your analysis. 

## Incremental Implementation

* Start by implementing the starting screen:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/coop_os_start.png" width=500>

* Next, implement program selection
  * Highlight the currently selected window in response to the appropriate function key
  * Highlight the currently selected program in response to arrow keys
* Then, implement process execution
  * I/O for the started process should appear in the appropriate window
* Finally, implement your schedulers

## Submissions
* Create a **private** GitHub repository for your cooperative kernel.
* Paste the repository URL into your Teams channel.
* Also post a PDF document to your Teams channel containing your analysis of
the scheduling alternatives.

## Assessment
* **Partial**: The user can execute and interact with a process.
* **Complete**: Meets all requirements given above.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).
