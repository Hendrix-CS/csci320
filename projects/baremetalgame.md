---
layout: work
type: Project
num: 6
worktitle: Bare Metal Game
---

Classic console video games such as [Space Invaders](https://en.wikipedia.org/wiki/Space_Invaders), 
[Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)), and
[Pac-man](https://en.wikipedia.org/wiki/Pac-Man) were implemented without an operating system.
The games mediated all hardware interaction by themselves.

In this project, you will use the [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os)
to develop a bare-metal video game. The graphical aspect of the game will be rendered in the VGA buffer.
You are encouraged to be creative in using VGA characters to represent your game graphics.

You are welcome to develop an original game or to create your own interpretation of a classic game.
As an example, feel free to reference [Ghost Hunter](https://github.com/gjf2a/ghost_hunter),
my own interpretation of a well-known classic.

## Interrupts

The primary purpose of this project is for you to gain experience writing software that handles
[hardware interrupts](https://os.phil-opp.com/hardware-interrupts/). When an event pertinent to the hardware
occurs, it notifies the CPU by signaling an interrupt. The CPU responds to the interrupt by suspending execution
of whatever code it is running and running the code designated for handling the interrupt. Naturally, 
interrupt-handling code should complete as quickly as possible so that the CPU can resume normal execution.


## Setup

The [Pluggable Interrupt OS](https://crates.io/crates/pluggable_interrupt_os) provides a convenient framework for
specifying to the CPU the code to be executed to handle each interrupt. 

I have created a [template](https://github.com/gjf2a/pluggable_interrupt_template) 
for you to use as a starting point for your projects. To start your project, clone 
the [Pluggable Interrupt Template](https://github.com/gjf2a/pluggable_interrupt_template) 
project. In order to build the project, you'll also need to install:
* [Qemu](https://www.qemu.org/)
* Nightly Rust:
  * `rustup override set nightly`
* `llvm-tools-preview`:
  * `rustup component add llvm-tools-preview`
* The [bootimage](https://github.com/rust-osdev/bootimage) tool:
  * `cargo install bootimage`
* On Windows:
  * `rustup component add rust-src --toolchain nightly-x86_64-pc-windows-msvc`
  
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

use crossbeam::atomic::AtomicCell;
use pc_keyboard::DecodedKey;
use pluggable_interrupt_os::{vga_buffer::clear_screen, HandlerTable};
use pluggable_interrupt_template::LetterMover;

#[no_mangle]
pub extern "C" fn _start() -> ! {
    HandlerTable::new()
        .keyboard(key)
        .timer(tick)
        .startup(startup)
        .cpu_loop(cpu_loop)
        .start()
}

static LAST_KEY: AtomicCell<Option<DecodedKey>> = AtomicCell::new(None);
static TICKED: AtomicCell<bool> = AtomicCell::new(false);

fn cpu_loop() -> ! {
    let mut kernel = LetterMover::default();
    loop {
        if let Ok(_) = TICKED.compare_exchange(true, false) {
            kernel.tick();
        }
        
        if let Ok(k) = LAST_KEY.fetch_update(|k| if k.is_some() {Some(None)} else {None}) {
            if let Some(k) = k {
                kernel.key(k);
            }
        }
    }
}

fn key(key: DecodedKey) {
    LAST_KEY.store(Some(key));
}

fn tick() {
    TICKED.store(true);
}

fn startup() {
    clear_screen();
}
```

The **_start()** function kicks everything off by placing references to our interrupt handling functions
in a **HandlerTable** object. Invoking **.start()** on the **HandlerTable**
sets up the interrupt handlers, then starts execution of the `cpu_loop()` function.

I created the [`LetterMover`](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/src/lib.rs)
`struct` to represent the application state. It is maintained inside of 
`cpu_loop()`. It gets updated in response to messages from the interrupt
handlers. Those messages are sent by updating shared `AtomicCell` objects.

Whenever a timer interrupt occurs, `tick()` changes `TICKED` to `true`. Whenever a
keyboard interrupt occurs, `key()` updates `LAST_KEY` to contain the most
recent keypress.

The `cpu_loop()` checks `TICKED` constantly. Whenever a new tick occurs,
it instructs the `LetterMover` to update its state accordingly. Similarly, 
whenever a new keypress appears, `cpu_loop()` relays that keystroke
to `LetterMover`. 

This shows the basic design that all of these projects should employ:
* Create a `main.rs` that sets up the interrupt handlers.
* Write a `cpu_loop()` function that contains the main data structures
  and monitors concurrent state for updates from interrupts.
* Write one-line handlers for the timer and keyboard that reference shared
  state that `cpu_loop()` can employ.
* Place all of the game functionality within the game-state object, defined in **lib.rs**.


Here is the rest of its code, found in its [`lib.rs`](https://github.com/gjf2a/pluggable_interrupt_template/blob/master/src/lib.rs) file:
```
#![no_std]

use num::Integer;
use pc_keyboard::{DecodedKey, KeyCode};
use pluggable_interrupt_os::vga_buffer::{
    is_drawable, plot, Color, ColorCode, BUFFER_HEIGHT, BUFFER_WIDTH,
};

use core::{
    clone::Clone,
    cmp::{min, Eq, PartialEq},
    iter::Iterator,
    marker::Copy,
    prelude::rust_2024::derive,
};

#[derive(Copy, Clone, Eq, PartialEq)]
pub struct LetterMover {
    letters: [char; BUFFER_WIDTH],
    num_letters: usize,
    next_letter: usize,
    col: usize,
    row: usize,
    dx: usize,
    dy: usize,
}

pub fn safe_add<const LIMIT: usize>(a: usize, b: usize) -> usize {
    (a + b).mod_floor(&LIMIT)
}

pub fn add1<const LIMIT: usize>(value: usize) -> usize {
    safe_add::<LIMIT>(value, 1)
}

pub fn sub1<const LIMIT: usize>(value: usize) -> usize {
    safe_add::<LIMIT>(value, LIMIT - 1)
}

impl Default for LetterMover {
    fn default() -> Self {
        Self {
            letters: ['A'; BUFFER_WIDTH],
            num_letters: 1,
            next_letter: 1,
            col: BUFFER_WIDTH / 2,
            row: BUFFER_HEIGHT / 2,
            dx: 0,
            dy: 0,
        }
    }
}

impl LetterMover {
    fn letter_columns(&self) -> impl Iterator<Item = usize> + '_ {
        (0..self.num_letters).map(|n| safe_add::<BUFFER_WIDTH>(n, self.col))
    }

    pub fn tick(&mut self) {
        self.clear_current();
        self.update_location();
        self.draw_current();
    }

    fn clear_current(&self) {
        for x in self.letter_columns() {
            plot(' ', x, self.row, ColorCode::new(Color::Black, Color::Black));
        }
    }

    fn update_location(&mut self) {
        self.col = safe_add::<BUFFER_WIDTH>(self.col, self.dx);
        self.row = safe_add::<BUFFER_HEIGHT>(self.row, self.dy);
    }

    fn draw_current(&self) {
        for (i, x) in self.letter_columns().enumerate() {
            plot(
                self.letters[i],
                x,
                self.row,
                ColorCode::new(Color::Cyan, Color::Black),
            );
        }
    }

    pub fn key(&mut self, key: DecodedKey) {
        match key {
            DecodedKey::RawKey(code) => self.handle_raw(code),
            DecodedKey::Unicode(c) => self.handle_unicode(c),
        }
    }

    fn handle_raw(&mut self, key: KeyCode) {
        match key {
            KeyCode::ArrowLeft => {
                self.dx = sub1::<BUFFER_WIDTH>(self.dx);
            }
            KeyCode::ArrowRight => {
                self.dx = add1::<BUFFER_WIDTH>(self.dx);
            }
            KeyCode::ArrowUp => {
                self.dy = sub1::<BUFFER_HEIGHT>(self.dy);
            }
            KeyCode::ArrowDown => {
                self.dy = add1::<BUFFER_HEIGHT>(self.dy);
            }
            _ => {}
        }
    }

    fn handle_unicode(&mut self, key: char) {
        if is_drawable(key) {
            self.letters[self.next_letter] = key;
            self.next_letter = add1::<BUFFER_WIDTH>(self.next_letter);
            self.num_letters = min(self.num_letters + 1, BUFFER_WIDTH);
        }
    }
}

```

The keyboard handler receives each character as it is typed. Keys representable as a `char`
are added to the moving string. The arrow keys change how the string is moving.

In order to implement wrapping around the sides of the screen, this implementation uses 
[modular numbers](https://docs.rs/bare_metal_modulo/1.2.5/bare_metal_modulo/). I have an
[alternative implementation](https://github.com/gjf2a/pluggable_interrupt_template_simplified) 
that uses modulo directly on integers rather than modular numbers. The effect is the same,
but you may find the alternative implementation a bit more transparent.
  
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
* Submit your GitHub URL via Teams.
* Be ready to present your game in class on Friday, March 14.
  * Presentation should consist of the following four slides:
    * Title slide
    * Overview of game
    * Overview of code structure
    * Key challenges overcome
  * Then give a brief (2 minute) live demo of the game.
  * Some presentations may take place on Monday, March 17.

## Assessment
* **Level 1**: 
  * Meets requirements 1, 2, and 3, and either requirement 4 or requirement 5.
* **Level 2**: 
  * Meets all requirements given above. 
  * Presentation given in class on March 14 or 17 when requested.
* **Level 3**:
  * Meets all Level 2 criteria.
  * In addition, the game demonstrates creativity or innovation in a striking way. 
    * Something comparable to [Ghost Hunter](https://github.com/gjf2a/ghost_hunter) 
      in complexity or engagement would probably suffice.
    * Consult with instructor prior to submission to determine if game scope is at this level.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).

------------------------------------------------------------------------
