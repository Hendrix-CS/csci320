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
specifying to the CPU the code to be executed to handle each interrupt. 

I have created a [template](https://github.com/gjf2a/pluggable_interrupt_template) 
for you to use as a starting point for your projects. To start your project, clone 
the [Pluggable Interrupt Template](https://github.com/gjf2a/pluggable_interrupt_template) 
project. In order to build the project, you'll also need to install:
* [Qemu](https://www.qemu.org/)
* Nightly Rust:
  * `rustup default nightly`
* `llvm-tools-preview`:
  * `rustup component add llvm-tools-preview`
* The [bootimage](https://github.com/rust-osdev/bootimage) tool:
  * `cargo install bootimage`
  
Once the template is up and running, you will be ready to implement your own interrupt handlers! Of course,
you'll want to change the project name and authors in 
[Cargo.toml](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/Cargo.toml), and you'll also 
want to set up your own GitHub repository for it.

The template project demonstrates a simple interactive program that uses both keyboard and timer interrupts.
When the user types a viewable key, it is added to a string in the middle of the screen.
When the user types an arrow key, the string begins moving in the indicated direction.
Here is its [`main.rs`](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/src/main.rs):

```
#![no_std]
#![no_main]

use lazy_static::lazy_static;
use spin::Mutex;
use pc_keyboard::DecodedKey;
use pluggable_interrupt_template::LetterMover;
use pluggable_interrupt_os::HandlerTable;

#[no_mangle]
pub extern "C" fn _start() -> ! {
    HandlerTable::new()
        .keyboard(key)
        .timer(tick)
        .start()
}

lazy_static! {
    static ref LETTERS: Mutex<LetterMover> = Mutex::new(LetterMover::new());
}


fn tick() {
    LETTERS.lock().tick();
}

fn key(key: DecodedKey) {
    LETTERS.lock().key(key);
}
```

The **_start()** function kicks everything off by placing references to our interrupt handling functions
in a **HandlerTable** object. Invoking **.start()** on the **HandlerTable**
starts execution. The PIOS sits back and loops endlessly, relying on the event handlers to
perform any events of interest or importance.

I created the [`LetterMover`](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/src/lib.rs)
`struct` to represent the application state. As interrupts are inherently concurrent, we wrap the object in a 
[`Mutex`](https://doc.rust-lang.org/book/ch16-03-shared-state.html). In order to delay constructing the 
object until it is first referenced, we employ the 
[Lazy Static](https://os.phil-opp.com/vga-text-mode/#lazy-statics) macro.

This shows the basic design that all of these projects should employ:
* Create a `main.rs` that sets up the interrupt handlers.
* Write one-line handlers for the timer and keyboard that reference a shared game-state object.
* Place all of the game functionality within the game-state object, defined in **lib.rs**.

The **tick()** function calls the `LetterMover::tick()` method after unlocking the object. 
Similarly, the **key()** function calls the `LetterMover::key()` method, again after unlocking
the object.

Here is the rest of its code, found in its [`lib.rs`](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/src/lib.rs) file:
```
#![cfg_attr(not(test), no_std)]

use bare_metal_modulo::{ModNum, ModNumIterator};
use pluggable_interrupt_os::vga_buffer::{BUFFER_WIDTH, BUFFER_HEIGHT, plot, ColorCode, Color, is_drawable};
use pc_keyboard::{DecodedKey, KeyCode};
use num::traits::SaturatingAdd;

#[derive(Copy,Debug,Clone,Eq,PartialEq)]
pub struct LetterMover {
    letters: [char; BUFFER_WIDTH],
    num_letters: ModNum<usize>,
    next_letter: ModNum<usize>,
    col: ModNum<usize>,
    row: ModNum<usize>,
    dx: ModNum<usize>,
    dy: ModNum<usize>
}

impl LetterMover {
    pub fn new() -> Self {
        LetterMover {
            letters: ['A'; BUFFER_WIDTH],
            num_letters: ModNum::new(1, BUFFER_WIDTH),
            next_letter: ModNum::new(1, BUFFER_WIDTH),
            col: ModNum::new(BUFFER_WIDTH / 2, BUFFER_WIDTH),
            row: ModNum::new(BUFFER_HEIGHT / 2, BUFFER_HEIGHT),
            dx: ModNum::new(0, BUFFER_WIDTH),
            dy: ModNum::new(0, BUFFER_HEIGHT)
        }
    }
```

This data structure represents the letters the user has typed, the total number of typed letters,
the position of the next letter to type, the position of the string, and its motion. Initially,
the string consists of the letter `A`, motionless, and situated in the middle of the screen.

The [`ModNum` data type](https://crates.io/crates/bare_metal_modulo) represents an integer 
(modulo m). It is very useful for keeping all of these values within the constraints of the 
VGA buffer.

```
    fn letter_columns(&self) -> impl Iterator<Item=usize> {
        ModNumIterator::new(self.col)
            .take(self.num_letters.a())
            .map(|m| m.a())
    }
```

Also from the [bare_metal_modulo](https://crates.io/crates/bare_metal_modulo) crate, the 
`ModNumIterator` data type starts at the specified value and loops around through the ring.
In this case, it takes just enough values to represent all of the columns to use when plotting
our string. Using `ModNum` ensures that all the column values are legal and wrap around 
appropriately. 

```
    pub fn tick(&mut self) {
        self.clear_current();
        self.update_location();
        self.draw_current();
    }

    fn clear_current(&self) {
        for x in self.letter_columns() {
            plot(' ', x, self.row.a(), ColorCode::new(Color::Black, Color::Black));
        }
    }
    
    fn update_location(&mut self) {
        self.col += self.dx;
        self.row += self.dy;
    }
    
    fn draw_current(&self) {
        for (i, x) in self.letter_columns().enumerate() {
            plot(self.letters[i], x, self.row.a(), ColorCode::new(Color::Cyan, Color::Black));
        }
    }
```

On each tick:
* Clear the current string.
* Update its position.
* Redraw the string in its new location.

```
    pub fn key(&mut self, key: DecodedKey) {
        match key {
            DecodedKey::RawKey(code) => self.handle_raw(code),
            DecodedKey::Unicode(c) => self.handle_unicode(c)
        }
    }

    fn handle_raw(&mut self, key: KeyCode) {
        match key {
            KeyCode::ArrowLeft => {
                self.dx -= 1;
            }
            KeyCode::ArrowRight => {
                self.dx += 1;
            }
            KeyCode::ArrowUp => {
                self.dy -= 1;
            }
            KeyCode::ArrowDown => {
                self.dy += 1;
            }
            _ => {}
        }
    }

    fn handle_unicode(&mut self, key: char) {
        if is_drawable(key) {
            self.letters[self.next_letter.a()] = key;
            self.next_letter += 1;
            self.num_letters = self.num_letters.saturating_add(&ModNum::new(1, self.num_letters.m()));
        }
    }
}
```

The keyboard handler receives each character as it is typed. Keys representable as a `char`
are added to the moving string. The arrow keys change how the string is moving.

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
* Nightly Rust:
  * `rustup default nightly`
* `llvm-tools-preview`:
  * `rustup component add llvm-tools-preview`
* The [bootimage](https://github.com/rust-osdev/bootimage) tool:
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