---
layout: work
type: Project
num: 3
worktitle: Advanced Shell Commands Using Rust
---

Implement the following shell commands as Rust programs:
* `findtext`: Output every line that contains a specified pattern. The first command-line argument is the fixed-string pattern. Remaining arguments are the names of the files to inspect.
* `order`: Works like `cat`, except the output lines must be sorted before being output. All lines from all files will be mixed together and then sorted. If the "-r" command-line argument is provided, they should be sorted in reverse order.

Implement the following shell command-line interpreter:
* `vssh`, the Very Simple SHell: 
  * Displays the [current working directory](https://doc.rust-lang.org/std/env/fn.current_dir.html) while awaiting user input.
  * If the user types `exit`, the program ends.
  * If the user types `cd [dir]`, change [current working directory](https://doc.rust-lang.org/std/env/fn.set_current_dir.html) accordingly.
  * If the user types a blank line, ignore it and display the prompt once again.
  * Execute any other command the user types by spawning a new process:
    * Be sure to include the [nix crate](https://crates.io/crates/nix) in `Cargo.toml` using the following line under `[dependencies]`:
      * `nix = {version = "0.26.2", features = ["process"]}`
	* Use [fork](https://docs.rs/nix/0.26.2/nix/unistd/fn.fork.html) to create the child process.
	* Within the child process, use [execvp](https://docs.rs/nix/0.26.2/nix/unistd/fn.execvp.html) to execute the command.
	* Within the parent process, use [waitpid](https://docs.rs/nix/0.26.2/nix/sys/wait/fn.waitpid.html) to wait for the child process to complete.
  * `vssh` **should not panic**. Be sure to explicitly handle every possible error.  
  * There is no need to implement pipes (`|`) or input/output redirection (`<` 
    and `>`). That is a topic for the next project.
* The `vssh` assignment was adapted from [materials](http://rust-class.org/pages/ps2.html) developed by [David Evans](http://www.cs.virginia.edu/~evans/) at the [University of Virginia](https://engineering.virginia.edu/departments/computer-science).	

Here is an example execution of `vssh`:

```
gjf2a@18837FDRL:/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ cargo run
   Compiling vssh v0.1.0 (/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh)   
   Finished dev [unoptimized + debuginfo] target(s) in 1.89s                                    
   Running `target/debug/vssh`                                                               
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ cd src                   
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh/src$ grep fn main.rs     
fn main() {                                                                             
fn get_input(prompt: &str) -> String {                                                     
fn run(command: &str) {                                                            
fn externalize(command: &str) -> Box<[CString]> {                 
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh/src$ cd ..
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ ls        
Cargo.lock  Cargo.toml  src  target  vssh.iml                           
/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$ exit 
gjf2a@18837FDRL:/mnt/c/Users/ferrer/Documents/Courses/2020_2S/CSCI320/Solutions/vssh$   
```

The `execvp` system call requires the command to be formatted as a fixed-size array of 
[c-style strings](https://doc.rust-lang.org/std/ffi/struct.CString.html). The function
below will perform this conversion for you:

```
fn externalize(command: &str) -> Vec<CString> {
    command.split_whitespace()
        .map(|s| CString::new(s).unwrap())
        .collect()
}
```

If the compiler requests a parameterized type for `execvp`, use `CString`. 

## Submissions
* You may place your files in the GitHub repository you used for the 
  previous project, or you can create a new one for this project. Make
  sure your repository is private, and that you add the instructor
  as a collaborator.
* Post the GitHub URL you would like me to examine in your private
  channel of the CSCI 320 Team.

## Assessment
* **Partial**: Correctly complete either `vssh` or both of `findtext` and `order`.
* **Complete**: All three programs correctly completed.

------------------------------------------------------------------------
