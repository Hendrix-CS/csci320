---
layout: work
type: Project
num: 9
worktitle: Game Kernel
---

Arcade consoles allow a user to select a game to play, play it, and when it
ends, select another game. In this project, you will implement a Game Kernel
that enables this functionality, plus a bit more. Specifically, your Game
Kernel will allow users to suspend a game in progress, resume a suspended game,
and even have multiple instances of the same game in progress at once.

Here is a screenshot of how the Game Kernel looks:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/Game_Kernel_In_Progress.png" width=500>

Here is a summary of the required functionality:
* When the Game Kernel starts, we see a starting screen with three lines of
instructions. The instructions read as follows:
  * `Type 's' to start a game`
  * `Type 'r' to resume a game`
  * `Type 'k' to end a game`
* Below the instructions is a list of all available games.
* One game is always highlighted. 
  * If the user types `s`, the highlighted game
  will start. 
  * The highlight is changed by using the up and down arrow keys.
* When a game is in progress, pressing the Escape key will pause the game
  and return to the starting screen.
* Paused games in progress are listed in the right column. 
  * The highlight moves to this column from the starting column using the left and
  right arrow keys. 
  * If the user types `r`, the highlighted game is resumed.
  * If the user types `k`, the highlighted game is terminated. Terminated games
    are no longer displayed in the column. All other running games retain
	their process IDs.