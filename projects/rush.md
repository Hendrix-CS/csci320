---
layout: work
type: Project
num: 4
worktitle: Unix Shell
---

## Description

Enhance [vssh]({{site.baseurl}}/projects/rust2.html) as follows:
1. If the line ends with the & symbol, it should run in the background. That is, your shell should not wait for it to terminate; the command line should immediately return. Your shell should print the PID of the process, so that the user may later manage it as needed. This is typically used for long-running programs that perform a lot of computation. It is most often used in conjunction with output redirection, as described in step 2.
2. If (prior to the & symbol, if present) the line ends with a > symbol that is immediately followed by a string, the command's output goes to the file named by the string. If the file does not exist, it will be created.
3. The line may contain two or more commands connected with the pipe symbol (|). If this happens, start a process for each command, setting up pipes to send the output of each left-hand command to the input of the following right-hand command. If the input has been redirected by the < symbol, then the leftmost process will receive the input from that file.
4. If (prior to the & symbol and > symbols, if present) the line ends with a < symbol that is immediately followed by a string, the command's input comes from the file named by the string. If the file does not exist, the command will be aborted.

This assignment was adapted from [materials](http://rust-class.org/pages/ps2.html) developed by [David Evans](http://www.cs.virginia.edu/~evans/) at the [University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

## Example Execution
```
gjf2a@18837FDRL:/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ cargo run
  Finished dev [unoptimized + debuginfo] target(s) in 0.06s
   Running `target/debug/vssh`
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ ls -l | grep Cargo | sort
-rwxrwxrwx 1 gjf2a gjf2a  240 Jan 14 22:40 Cargo.toml
-rwxrwxrwx 1 gjf2a gjf2a 2088 Jan 14 22:40 Cargo.lock
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ ls -l | grep Cargo > output.txt
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ cat < output.txt
-rwxrwxrwx 1 gjf2a gjf2a 2088 Jan 14 22:40 Cargo.lock
-rwxrwxrwx 1 gjf2a gjf2a  240 Jan 14 22:40 Cargo.toml
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ ls -l
total 4
-rwxrwxrwx 1 gjf2a gjf2a 2088 Jan 14 22:40 Cargo.lock
-rwxrwxrwx 1 gjf2a gjf2a  240 Jan 14 22:40 Cargo.toml
-rwxrwxrwx 1 gjf2a gjf2a  108 Jan 16 00:14 output.txt
-rwxrwxrwx 1 gjf2a gjf2a  491 Jan 14 22:40 vssh.iml
drwxrwxrwx 1 gjf2a gjf2a  512 Jan 15 23:55 src
drwxrwxrwx 1 gjf2a gjf2a  512 Jan 14 23:47 target
-rwxrwxrwx 1 gjf2a gjf2a   50 Jan 15 00:24 test.out
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ ls -l &
child in background: 12817
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ total 4
-rwxrwxrwx 1 gjf2a gjf2a 2088 Jan 14 22:40 Cargo.lock
-rwxrwxrwx 1 gjf2a gjf2a  240 Jan 14 22:40 Cargo.toml
-rwxrwxrwx 1 gjf2a gjf2a  108 Jan 16 00:14 output.txt
-rwxrwxrwx 1 gjf2a gjf2a  491 Jan 14 22:40 vssh.iml
drwxrwxrwx 1 gjf2a gjf2a  512 Jan 15 23:55 src
drwxrwxrwx 1 gjf2a gjf2a  512 Jan 14 23:47 target
-rwxrwxrwx 1 gjf2a gjf2a   50 Jan 15 00:24 test.out

/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ cd src
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh/src$ grep fn main.rs | sort
    fn new(line: &str) -> Self {
	fn run(&self) {
	fn run_pipeline(&self) {
fn execute(command: &str, output_descriptor: i32) {
fn externalize(command: &str) -> Box<[CString]> {
fn get_input(prompt: &str) -> String {
fn main() {
fn pipeline_stage(command: &str, out: i32) -> i32 {	    
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh/src$ exit 
gjf2a@18837FDRL:/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$
```

## Design Hints

* Implementing a shell is simplified by separating the parsing of the command line from its execution. I 
recommend creating a `struct` to represent the different components of the parsed command line:
  * Whether it is a background command.
  * Its output file, if redirected.
  * Its input file, if redirected.
  * A vector of its pipelined commands.
* Redirecting standard output can make debugging difficult; I recommend using 
  [eprintln!](https://doc.rust-lang.org/std/macro.eprintln.html), which prints to standard error.
* Break the execution of the command line into a series of functions:
  * The top-level execution function [forks](https://docs.rs/nix/0.19.1/nix/unistd/fn.fork.html).
    * Parent waits, unless it is a background process.
	* Child calls a function to execute a pipeline.
  * The pipeline execution function:
    * Sets up a variable to track the current output file descriptor.
	  * If output has been redirected to a file, 
	    [open](https://docs.rs/nix/0.19.1/nix/fcntl/fn.open.html) 
		[it](https://man7.org/linux/man-pages/man2/open.2.html) and use its file descriptor.
	  * Otherwise, set it to 1, the file descriptor for standard output.
	* Loops through the commands in the pipeline, starting with the **last** one.
	  * The last command waits for input from its predecessor, so it has to start first.
	  * The first command in the pipeline is a special case; deal with it after the loop ends.
    * For each command in the loop:
      * Call a pipeline stage function, sending it the current command and current output 
	    file descriptor and receiving from it an updated output file descriptor.
    * When the loop is over:
      * Redirect input to be received from a file, if necessary.
	  * Redirect output to the current output file descriptor.
      * Execute the first command in the pipeline.
  * The pipeline stage function:
    * Create a [pipe](https://docs.rs/nix/0.19.1/nix/unistd/fn.pipe.html). The pipe will 
	  receive data from the current command's predecessor, and send data to the current 
	  command. 	  
    * Use [fork](https://docs.rs/nix/0.19.1/nix/unistd/fn.fork.html) to create the child process.
	  * In the parent (corresponding to the current command):
	    * Close the pipe's input. It is unnecessary here, as the pipe will receive data from
		  the preceding command.
	    * Use [dup2](https://docs.rs/nix/0.19.1/nix/unistd/fn.dup2.html) to redirect the process input to the pipe output.
		* Use [dup2](https://docs.rs/nix/0.19.1/nix/unistd/fn.dup2.html) to redirect the process output to the current output file descriptor.
		* Execute the current command.
      * In the child (corresponding to all commands in the pipeline that precede the current command):
	    * Close the pipe's output. It is unnecessary here, as the pipe will send data to 
		  the current command.
		* Return the pipe's input, so it can receive output from the preceding command in the pipeline.


## Submissions
* Push your enhancements to the same GitHub repository you used for `vssh` in the previous assignment.

## Assessment
* **Partial**: Correctly complete any two enhancements.
* **Complete**: All four enhancements correctly completed.

------------------------------------------------------------------------
