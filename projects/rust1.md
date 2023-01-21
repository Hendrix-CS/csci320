---
layout: work
type: Project
num: 2
worktitle: Creating Shell Commands Using Rust
---

## Getting Started

If using Windows Subsystem for Linux (WSL), start with:
```
sudo apt install build-essential
```

Install Rust:
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Install [Visual Studio Code](https://code.visualstudio.com/). Click on the Extensions icon: ![Extensions Icon](/"{{site.baseurl}}/assets/images/ExtensionsIcon.PNG)

Install:
* `rust-analyzer`
* `Error Lens`
* `Search crates.io`
* `Even Better TOML`
* (On WSL) `Remote Development`

You can open a Unix shell within Visual Studio Code with `` CTRL-` ``.

## Creating a Cargo Project

From a command line, type:
```
cargo new shell
cd shell/src/
mkdir bin
mv main.rs bin/cmd.rs
```

Then open VSCode and open the `shells` folder. Open `bin/cmd.rs` and paste in the code below:

```
fn main() {
    for arg in std::env::args() {
        println!("{arg}");
    }
}
```

To execute this program in the shell:

```
cargo run --bin cmd a b c
```

## Assignment

Implement the following shell commands as Rust programs. 
You might find the [fs module](https://doc.rust-lang.org/std/fs/index.html) useful in 
writing many of these programs:

* `dir`: Prints out all of the names of the files and directories in the current directory. It will not employ any command-line arguments.
* `destroy`: Delete every file in the list of command-line arguments.
* `newname`: This program expects two command-line arguments. It will give a "usage" message if it does not receive them. It will change the name of the file given by the first argument to be the name given by the second argument.
* `duplicate`: This program also expects two command-line arguments. It will give a "usage" message if it does not receive them. It will make a copy of the file given by the first argument with the name given by the second argument.
* `start`: Prints out the first ten lines of each file listed in the command-line arguments. If the first argument begins with a dash, use the number immediately following the dash instead of ten.
* `counter`: Prints out the number of words, lines, and characters for each file listed in its command-line arguments. If the first argument begins with a dash, the letters "w", "l", and "c" immediately following the dash indicate which of words, lines, and characters get displayed.

## Submissions
* Share the `shells` folder as a **private** GitHub repository.
* Submit your GitHub URL via Teams.

## Assessment
* **Partial**: Any three programs correctly completed.
* **Complete**: All six programs correctly completed.

------------------------------------------------------------------------
