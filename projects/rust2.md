---
layout: work
type: Project
num: 3
worktitle: Advanced Shell Commands Using Rust
---

## Description

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
    * Be sure to include the [nix crate](https://crates.io/crates/nix) in `Cargo.toml`. 
	* Use [fork](https://docs.rs/nix/0.19.1/nix/unistd/fn.fork.html) to create the child process.
	* Within the child process, use [execvp](https://docs.rs/nix/0.19.1/nix/unistd/fn.execvp.html) to execute the command.
	  * Convert the command to [CString](https://doc.rust-lang.org/std/ffi/struct.CString.html) objects before sending them on.
	* Within the parent process, use [waitpid](https://docs.rs/nix/0.19.1/nix/sys/wait/fn.waitpid.html) to wait for the child process to complete.

## Submissions
* Create a separate **private** GitHub repository for each of these programs.
* [Submit GitHub URLs](https://docs.google.com/forms/d/e/1FAIpQLSee88rfIgOzg1MsoFPNPBncW76kfVXSu8eYElAgpI9WgLsiLg/viewform?usp=sf_link)

## Assessment
* **Partial**: Correctly complete either `vssh` or both of `findtext` and `order`.
* **Complete**: All three programs correctly completed.

------------------------------------------------------------------------
