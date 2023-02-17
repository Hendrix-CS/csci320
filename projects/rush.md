---
layout: work
type: Project
num: 4
worktitle: Unix Shell
---

Create a new version of [vssh1]({{site.baseurl}}/projects/rust2.html) 
that is enhanced in the following ways. This new version should be a 
separate executable called `vssh2`.
1. If the line ends with the `&` symbol, it should run in the background. That is, your shell should not wait for it 
to terminate; the command line should immediately return. Your shell should print the PID of the process, so that 
the user may later manage it as needed. This is typically used for long-running programs that perform a lot of 
computation. It is most often used in conjunction with output redirection, as described in step 3.
2. The line may contain two or more commands connected with the pipe symbol (`|`). If this happens, start a process 
for each command, setting up pipes to send the output of each left-hand command to the input of the following 
right-hand command. 
3. The last command in the pipeline (or the only command, if there is no pipeline) may be followed by the `>` symbol
and a filename. The command's output should be stored in the designated file. If the file does not exist, 
it should be created.
4. The first command in the pipeline (or the only command, if there is no pipeline) may be followed by the `<` symbol
and a filename. The command's input should be taken from the designated file. If the file does not exist,
the command should abort.

## Example Execution
```
/home/gjf2a/solutions320$ ls -l | grep Cargo | sort
-rw-r--r-- 1 gjf2a gjf2a  262 Feb 12 12:31 Cargo.toml
-rw-r--r-- 1 gjf2a gjf2a 5264 Feb 12 12:31 Cargo.lock
/home/gjf2a/solutions320$ ls -l | grep Cargo > output.txt
/home/gjf2a/solutions320$ cat < output.txt
-rw-r--r-- 1 gjf2a gjf2a 5264 Feb 12 12:31 Cargo.lock
-rw-r--r-- 1 gjf2a gjf2a  262 Feb 12 12:31 Cargo.toml
/home/gjf2a/solutions320$ ls -l
total 32
-rw-r--r-- 1 gjf2a gjf2a 5264 Feb 12 12:31 Cargo.lock
-rw-r--r-- 1 gjf2a gjf2a  262 Feb 12 12:31 Cargo.toml
-rw------- 1 gjf2a gjf2a  108 Feb 11 10:21 grep_test.out
-rw------- 1 gjf2a gjf2a  108 Feb 15 09:08 output.txt
drwxr-xr-x 3 gjf2a gjf2a 4096 Feb 10 13:21 src
drwxr-xr-x 3 gjf2a gjf2a 4096 Feb 10 13:21 target
-rw------- 1 gjf2a gjf2a  106 Feb 11 10:22 toml.out
/home/gjf2a/solutions320$ ls -l &
Starting background process 1871
/home/gjf2a/solutions320$ total 32
-rw-r--r-- 1 gjf2a gjf2a 5264 Feb 12 12:31 Cargo.lock
-rw-r--r-- 1 gjf2a gjf2a  262 Feb 12 12:31 Cargo.toml
-rw------- 1 gjf2a gjf2a  108 Feb 11 10:21 grep_test.out
-rw------- 1 gjf2a gjf2a  108 Feb 15 09:08 output.txt
drwxr-xr-x 3 gjf2a gjf2a 4096 Feb 10 13:21 src
drwxr-xr-x 3 gjf2a gjf2a 4096 Feb 10 13:21 target
-rw------- 1 gjf2a gjf2a  106 Feb 11 10:22 toml.out
cd src
/home/gjf2a/solutions320/src$ cd bin
/home/gjf2a/solutions320/src/bin$ grep fn vssh2.rs | sort
    fn default() -> Self {
    fn execute_pipeline(&self) -> anyhow::Result<()> {
    fn final_input_fd(&self) -> anyhow::Result<i32> {
    fn from_str(s: &str) -> Result<Self, Self::Err> {
    fn initial_output_fd(&self) -> anyhow::Result<i32> {
fn disassemble_redirect(pipes: &mut Vec<String>, i: usize, redirector: char) -> Option<String> {
fn execute(cmd: &str) {
fn externalize(command: &str) -> Vec<CString> {
fn main() {
fn process_next_line() -> anyhow::Result<Status> {
fn run_command(command: &str) -> anyhow::Result<()> {
fn run_stage(cmd: &str, output_fd: i32) -> anyhow::Result<i32> {
/home/gjf2a/solutions320/src/bin$ cat < vssh2.rs | sort | tail -8 > eight.out
/home/gjf2a/solutions320/src/bin$ cat eight.out
}
}
}
}
}
}
}
}
/home/gjf2a/solutions320/src/bin$ cd ../..
/home/gjf2a/solutions320$ cat < Cargo.toml > toml2.out
/home/gjf2a/solutions320$ diff Cargo.toml toml2.out 
/home/gjf2a/solutions320$ exit
```

## Design Hints

* Implementing a shell is simplified by separating the parsing of the command line from its execution. I 
recommend creating a `struct` to represent the different components of the parsed command line:
  * Whether it is a background command.
  * Its output file, if redirected.
  * Its input file, if redirected.
  * A vector of its pipelined commands.
* Here is one approach to parsing the command:
  * Check if it ends with an ampersand (`&`). If so, set the background command flag to `true`, and shave the `&` from the end.
  * Split the string based on the `|` symbol, and place the results into a vector.
    * Be sure to use `.to_string()` to convert them to fully owned objects, not borrowed objects.
  * Check the last element to see if it contains the `>` symbol. If so, put the output filename into your `struct`, 
    then remove it from the command entry.
  * Check the first element to see if it contains the `<` symbol. If so, put the input filename into your `struct`, 
    then remove it from the command entry.
* Redirecting standard output can make debugging difficult; I recommend using 
  [eprintln!](https://doc.rust-lang.org/std/macro.eprintln.html), which prints to standard error.
* Break the execution of the command line into a series of functions:
  * The top-level execution function [forks](https://docs.rs/nix/0.19.1/nix/unistd/fn.fork.html).
    * Parent waits, unless it is a background process.
	* Child calls a function to execute a pipeline.
  * The pipeline execution function:
    * Sets up a variable to track the current output file descriptor.
	  * If output has been redirected to a file, 
	    [open](https://docs.rs/nix/0.19.1/nix/fcntl/fn.open.html) that
		[file](https://man7.org/linux/man-pages/man2/open.2.html) and use its file descriptor.
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
    * Creates a [pipe](https://docs.rs/nix/0.19.1/nix/unistd/fn.pipe.html). The pipe will 
	  receive data from the current command's predecessor, and send data to the current 
	  command. 	  
    * Uses [fork](https://docs.rs/nix/0.19.1/nix/unistd/fn.fork.html) to create the child process.
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

## Acknowledgement

This assignment was adapted from [materials](http://rust-class.org/pages/ps2.html) developed by 
[David Evans](http://www.cs.virginia.edu/~evans/) at the 
[University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

------------------------------------------------------------------------
