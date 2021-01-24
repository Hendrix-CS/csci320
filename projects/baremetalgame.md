---
layout: work
type: Project
num: 8
worktitle: Bare Metal Game
---

Classic early video games such as [Space Invaders](https://en.wikipedia.org/wiki/Space_Invaders), 
[Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)), and
[Pac-man](https://en.wikipedia.org/wiki/Pac-Man) were implemented without an operating system.
The games mediated all hardware interaction by themselves.

In this project, you will use the [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os)
to develop a bare-metal video game. The graphical aspect of the game will be rendered in the VGA buffer.
You are encouraged to be creative in using VGA characters to represent your game graphics.

You are welcome to develop an original game or to create your own interpretation of a classic game.
As an example, feel free to reference [Ghost Hunter](https://github.com/gjf2a/ghost_hunter),
my own interpretation of a well-known classic.

Unlike our other projects, for this project you are welcome to work in a team of up to three students.

## Interrupts

The primary purpose of this project is for you to gain experience writing software that handles
[hardware interrupts](https://os.phil-opp.com/hardware-interrupts/). When an event pertinent to the hardware
occurs, it notifies the CPU by signaling an interrupt. The CPU responds to the interrupt by suspending execution
of whatever code it is running and running the code designated for handling the interrupt. Naturally, 
interrupt-handling code should complete as quickly as possible so that the CPU can resume normal execution.

This project will be very different in flavor, because **all** of the code you write will be executed by 
interrupt handlers. You will create two interrupt handlers for this project:
* Your **keyboard interrupt handler** will update the game based on player input.
* Your **timer interrupt handler** will update the game based on time-dependent gameplay elements of your design.

## Setup

The [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os) provides a convenient framework for
specifying to the CPU the code to be executed to handle each interrupt. Here is a 
[minimal example](https://github.com/gjf2a/pluggable_interrupt_template):

```
#![no_std]
#![no_main]

use pc_keyboard::DecodedKey;
use pluggable_interrupt_os::HandlerTable;
use pluggable_interrupt_os::print;

#[no_mangle]
pub extern "C" fn _start() -> ! {
    HandlerTable::new()
        .keyboard(key)
        .timer(tick)
        .start()
}

fn tick() {
    print!(".");
}

fn key(key: DecodedKey) {
    match key {
        DecodedKey::Unicode(character) => print!("{}", character),
        DecodedKey::RawKey(key) => print!("{:?}", key),
    }
}
```

As there is no operating system, there is nothing to call `main()`.  The `_start()` function
[replaces the operating system's entry point](https://os.phil-opp.com/freestanding-rust-binary/#overwriting-the-entry-point) 
with our own code. Within `_start()`, we set up a `HandlerTable` object. We assign `tick()` as the timer 
interrupt handler and `key()` as the keyboard interrupt handler. 

Here is the `main.rs` for [Ghost Hunter](https://github.com/gjf2a/ghost_hunter):
```
#![no_std]
#![no_main]

use lazy_static::lazy_static;
use spin::Mutex;
use ghost_hunter_core::GhostHunterGame;
use ghost_hunter::MainGame;
use pluggable_interrupt_os::HandlerTable;

use pc_keyboard::DecodedKey;

lazy_static! {
    static ref GAME: Mutex<MainGame> = Mutex::new(GhostHunterGame::new());
}

#[no_mangle]
pub extern "C" fn _start() -> ! {
    HandlerTable::new()
        .keyboard(key)
        .timer(tick)
        .start()
}

fn tick() {
    ghost_hunter::tick(&mut GAME.lock());
}

fn key(key: DecodedKey) {
    GAME.lock().key(key);
}
```

The `start()` function is identical to the previous example; it is the handlers that differ. Both handlers
update a [GhostHunterGame](https://github.com/gjf2a/ghost_hunter_core/blob/master/src/lib.rs) object.
As interrupts are inherently concurrent, we wrap the object in a 
[`Mutex`](https://doc.rust-lang.org/book/ch16-03-shared-state.html). In order to delay constructing the 
object until it is first referenced, we employ the 
[Lazy Static](https://os.phil-opp.com/vga-text-mode/#lazy-statics) macro.

This shows the basic design that all of these projects should employ:
* Create a `main.rs` that sets up the interrupt handlers.
* Write one-line handlers for the timer and keyboard that reference a shared game-state object.
* Place all of the game functionality within the game-state object.

To get started, clone the [Pluggable Interrupt Template](https://github.com/gjf2a/pluggable_interrupt_template) 
project. In order to build the project, you'll also need to install:
* [Qemu](https://www.qemu.org/)
* Nightly Rust. To install:
  * `rustup default nightly`
* `llvm-tools-preview`. To install:
  * `rustup component add llvm-tools-preview`
* The [bootimage](https://github.com/rust-osdev/bootimage) tool. To install it:
  * `cargo install bootimage`
  
Once the template is up and running, you will be ready to implement your own interrupt handlers! Of course,
you'll want to change the project name and authors in 
[Cargo.toml](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/Cargo.toml), and you'll also 
want to set up your own GitHub repository for it.
  
## Requirements

This project is very flexible in its requirements. A successful submission will:
1. Run in the Qemu x86 virtual machine without any supporting operating system.
2. Be built upon the [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os).
3. Only use `#[no_std]` Rust features and crates.
4. Enable the player to control a graphically depicted avatar using the keyboard.
5. Include gameplay elements that advance based on clock ticks and cause the game to eventually end if the player
  does not react to them appropriately.
6. Run indefinitely without any panics.
7. Allow the user to restart the game when it ends.
8. Display the user's current score.

## Submissions
* Create a **public** GitHub repository for your bare metal game.
* [Submit the repository URL](https://docs.google.com/forms/d/e/1FAIpQLSdNMxeqYMW7Awk7GFseKOx6E_VWaE2Ft9lg7Fdw6AiH-JxXtw/viewform?usp=sf_link)

## Assessment
* **Partial**: Meets requirements 1, 2, and 3, and either requirement 4 or requirement 5.
* **Complete**: Meets all requirements given above.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).

------------------------------------------------------------------------
