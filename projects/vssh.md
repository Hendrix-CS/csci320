---
layout: work
type: Project
num: 4
worktitle: Unix Shell
---

## Level 1: Forking processes

Implement `vssh`, the Very Simple SHell: 
* Create `src/bin/vssh.rs` in the `part1` project.
* Displays the [current working directory](https://doc.rust-lang.org/std/env/fn.current_dir.html) while awaiting user input.
* If the user types `exit`, the program ends.
* If the user types `cd [dir]`, change [current working directory](https://doc.rust-lang.org/std/env/fn.set_current_dir.html) accordingly.
* If the user types a blank line, ignore it and display the prompt once again.
* Execute any other command the user types by spawning a new process:
* Be sure to include the [nix crate](https://crates.io/crates/nix) in `Cargo.toml` using the following line under `[dependencies]`:
  * `nix = "0.26"`
  * Do not use a later version of `nix`; some backwards-incompatible changes make completing
    this assignment difficult.
* Use [fork](https://docs.rs/nix/latest/nix/unistd/fn.fork.html) to create the child process.
* Within the child process, use [execvp](https://docs.rs/nix/latest/nix/unistd/fn.execvp.html) to execute the command.
* Within the parent process, use [waitpid](https://docs.rs/nix/latest/nix/sys/wait/fn.waitpid.html) to wait for the child process to complete.
* If the line ends with the `&` symbol, the child process should run in the background. That is, your shell should not wait for it 
to terminate; the command line should immediately return. Your shell should print the PID of the process, so that 
the user may later manage it as needed. This is typically used for long-running programs that perform a lot of 
computation. 
* `vssh` **should not panic**. Be sure to explicitly handle every possible error.  

Here is an example execution of `vssh`:

```
gjf2a@20003LPUX:~/solutions320$ cargo run --bin vssh
   Compiling solutions320 v0.1.0 (/home/gjf2a/solutions320)
    Finished dev [unoptimized + debuginfo] target(s) in 1.75s
     Running `target/debug/vssh`
/home/gjf2a/solutions320$ cd src/bin
/home/gjf2a/solutions320/src/bin$ grep fn vssh.rs
fn main() {
fn process_next_line() -> anyhow::Result<Status> {
fn run_command(command: &str) -> anyhow::Result<()> {
fn externalize(command: &str) -> Vec<CString> {
/home/gjf2a/solutions320/src/bin$ cd ..
/home/gjf2a/solutions320/src$ cd ..
/home/gjf2a/solutions320$ ls
Cargo.lock  Cargo.toml  grep_test.out  src  target  toml.out
/home/gjf2a/solutions320$ exit
```

The `execvp` system call requires the command to be formatted as a fixed-size array of 
[c-style strings](https://doc.rust-lang.org/std/ffi/struct.CString.html). Here is our
example from class that demonstrates how to create `CString` objects for this purpose:
```
let mut argv = Vec::new();
for arg in ["wc", "src/bin/fork3.rs"] {
    argv.push(CString::new(arg).unwrap());
}
```

If the compiler requests a parameterized type for `execvp`, use `CString`. 

## Level 2: I/O redirection to/from files
1. A shell command may be followed by the `<` symbol
and a filename. The command's input should be taken from the designated file. If the file does not exist,
the command should abort. This is known as **input redirection**.
2. A shell command may also be followed by the `>` symbol
and a filename. The command's output should be stored in the designated file. If the file does not exist, 
it should be created. This is known as **output redirection**.
3. Both options may be combined in a single command. In that case, the input redirection
should be first.

### Example Execution

```
ferrer@20003LPUX:~/solutions320$ cargo run --bin vssh
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/vssh`
/home/ferrer/solutions320$ ls -lth > listing.out
/home/ferrer/solutions320$ cat < listing.out
total 44K
-rw------- 1 ferrer ferrer    0 Feb 12 08:35 listing.out
-rw-r--r-- 1 ferrer ferrer  293 Feb 12 08:31 Cargo.toml
drwxr-xr-x 3 ferrer ferrer 4.0K Feb 12 08:22 target
-rw-r--r-- 1 ferrer ferrer  15K Feb 12 08:22 Cargo.lock
-rw-r--r-- 1 ferrer ferrer  667 Feb 12 08:22 bare_metal_modulo
-rw-r--r-- 1 ferrer ferrer   49 Feb 12 08:22 baroque_hoedown.txt
-rw-r--r-- 1 ferrer ferrer  108 Feb 12 08:22 grep_test.out
drwxr-xr-x 3 ferrer ferrer 4.0K Feb 12 08:22 src
-rw-r--r-- 1 ferrer ferrer  106 Feb 12 08:22 test
/home/ferrer/solutions320$ 
```

## Level 3: Pipelines
1. The line may contain two or more commands connected with the pipe symbol (`|`). If this happens, start a process 
for each command, setting up pipes to send the output of each left-hand command to the input of the following 
right-hand command. 
2. The last command in the pipeline may be followed by the `>` symbol
and a filename. The command's output should be stored in the designated file. If the file does not exist, 
it should be created.
3. The first command in the pipeline may be followed by the `<` symbol
and a filename. The command's input should be taken from the designated file. If the file does not exist,
the command should abort.

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

## Submissions
* Share the `part1` project as a **private** GitHub repository.
* Submit your GitHub URL via Teams.

## Assessment
* **Level 1**: Basic `vssh` implementation.
* **Level 2**: I/O redirection.
* **Level 3**: Pipelines.

## Acknowledgement

This assignment was adapted from [materials](http://rust-class.org/pages/ps2.html) developed by 
[David Evans](http://www.cs.virginia.edu/~evans/) at the 
[University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

------------------------------------------------------------------------
