---
layout: work
type: Project
num: 10
worktitle: Very Simple Kernel
---

## Overview

The Very Simple Kernel is, as its name implies, a simple but functional operating
system. It has the following features:

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

After completing Step 1, the kernel should look like this:

<img src="https://hendrix-cs.github.io/csci320/assets/images/vsk_step_1.png" width=500>

## Step 2: Incorporating the File System

* Add a `FileSystem` object to your kernel.
  * Maximum filename length: 10
  * Maximum number of files: 30
  * [Tell them the other constant stats to use]
* Add a `list()` method to your file system.
  * Each window should display the names of all of the files in the file system,
    in three columns.
* When `F5` is selected, the user can enter a filename of up to 12 characters.
  * When the user types the backspace (Unicode ``\u{8}``), it erases the previous 
    character.
* When the user hits one of the other function keys, it switches to the
  designated buffer and activates the editor. 
  * The filename appears as part of the window header, after the function key.
  * As with the filename editing, each keystroke appears in the appropriate window,
    with the backspace operating properly as well.
  * Entering `F6` closes the file.

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
