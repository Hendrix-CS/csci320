---
layout: work
type: Project
num: 10
worktitle: Cooperative Multitasking Kernel
---

## Overview

In a cooperative multitasking environment, each concurrent task voluntarily yields
control to the CPU at certain prearranged times. A kernel with cooperative 
multitasking is significantly easier to implement than one with preemptive 
multitasking, so our focus for this project will be to assume cooperative 
multitasking.

## A State Machine Model for Cooperative Multitasking

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
  
When a keyboard interrupt occurs:
* `F1`, `F2`, `F3`, `F4`: Switch to the appropriate process/window
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

<!--
At this point, I think we will give the students the following:
* All of main.rs.
* First 68 lines of lib.rs.
* Declaration of the Kernel struct (without its data elements).
* impl of Kernel struct with headers of public methods.
  * They will all be unimplemented!().
-->

Here is a screenshot of how the Cooperative Multitasking Kernel looks:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/coop_os_four_procs.png" width=500>

In this screenshot:
* Process `F1` has completed. Its result is displayed, and the user can select to run
  a new process in that space.
* Processes `F2` and `F3` are in progress.
* Process `F4` is blocked awaiting user input.

## Submissions
* Create a **private** GitHub repository for your cooperative kernel.
* Paste the repository URL into your Teams channel.

## Assessment
* **Complete**: Meets all requirements given above.
* **Partial**: Sincere attempt to meet requirements, but incomplete in some way.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).