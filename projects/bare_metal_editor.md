---
layout: work
type: Project
num: 7
worktitle: Bare-Metal Windowing Editor
---

Starting with this project, we will create SWIM (Simple WIndowing Machine), a basic but functional
operating system. 

For **Level 1** credit:
* The VGA buffer contains a text editor with the following capabilities:
  * There is a cursor denoting where the next text character typed will appear.
  * When the user types a viewable character, it appears at the location of the cursor, and the cursor
    itself moves to the next column.
  * At the end of a row, the cursor moves to the start of the next row.
  * Typing the **Enter** key also moves the cursor to the start of the next row.
  
For **Level 2** credit:
* The VGA buffer contains **four** text editing windows, each of approximately equal size.
* Each window has an outline of period (`.`) characters.
* Each window has a header with one of `F1`, `F2`, `F3`, or `F4` in the center.
* Initially, the `F1` window is active.
* The currently active window should have a color-highlighted outline.
* The currently active window is where keystrokes appear.

For **Level 3** credit, each window should have the following additional capabilities:
* The backspace or delete key removes the character before the cursor, and moves the cursor one column
to the left. If the cursor is in column 0 and not at row 0, backspace will move the cursor to the previous row.
* A document may contain four times as many rows as a window. If the user types beyond the last visible row
(either from going past the last column or typing the **Enter** key), the window should **scroll**. That is, the
top line of text will disappear, and the remaining lines of text will all move up one row.
* The user can move the cursor around using the arrow keys. If the left or right arrow key moves the cursor past
the edge of the window, it should wrap around to the other side. If the up or down arrow key moves the cursor 
past the top or bottom of the window, it should scroll in the appropriate direction.

Here is an image of what the windowing editor should look like:

<img src="https://hendrix-cs.github.io/csci320/assets/images/swim_part_1_4_windows.png" width=500>

### Design suggestions
* This can be built atop the `pluggable_interrupt_template` project, just like the bare metal game.
* As with the game, it should have a central `struct` to represent the user interface as a whole.
* Make heavy use of constants for values like the window height and width, document height, starting locations
of windows, and so forth.
* Create an additional `struct` to represent an individual document. For **Level 1** and **Level 2**, this 
`struct` really only needs to represent the cursor position and window boundaries, as the text itself can be 
represented exclusively within the VGA buffer. For **Level 3**, this `struct` will need to maintain a 
representation of the entire document, in order to recover text hidden by scrolling.
* For **Level 2** and **Level 3**, the central `struct` should have an array of four document objects.
  * It should then have a `usize` to denote which of these is the active window.

## Submission
* Create a new `GitHub` repository for this project. It will also serve as your repository for Project 10.

## Assessment
* **Level 1**
  * Editor works in a single window
* **Level 2**
  * Four windows, each with a working editor
* **Level 3**
  * Arrow keys, delete keys, and scrolling all work.
