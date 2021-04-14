---
layout: work
type: Project
num: 10
worktitle: Cooperative Multitasking Kernel
---

## Overview

In a cooperative multitasking environment, each concurrent task voluntarily yields
control to the CPU at certain prearranged times. A kernel with cooperative 
multitasking is significantly easier to implement than one with preemptive 
multitasking, so our focus for this project will be to assume cooperative 
multitasking.

## A State Machine Model for Cooperative Multitasking

Each task that is run by our kernel is a **state machine**. At each time step,
each state machine can perform one of the following actions:
* Request keyboard input
* Request that output be printed to the screen
* Perform one step of its algorithm

The kernel runs up to four tasks. Each task has its own subwindow for input and
output. In the background, the kernel runs the following algorithm:

	loop indefinitely
		Ask the scheduler which process to run
		Run one instruction for the selected process
		
The effect of running an instruction depends upon its type:
* Input instruction: 
  * Process blocks, awaiting input
* Output instruction: 
  * Kernel outputs data from process
* Update instruction: 
  * Kernel instructs process to update itself by one computation step
  * Process yields control back to the kernel after completing this step
  
When a keyboard interrupt occurs:
* `F1`, `F2`, `F3`, `F4`: Switch to the appropriate process/window
* If no program is running in the current window:
  * `ArrowUp`, `ArrowDown`: Switch between candidate programs to run
  * `Enter`: Start the currently selected program
* All others:
  * Store the key in a buffer for the current process
  * If a newline, send the string in the buffer to the process, and clear the buffer
  
When a timer interrupt occurs:
* Process status side window is updated
  * For each process, it displays the total number of updates since
    it started running

<!--
At this point, I think we will give the students the following:
* All of main.rs.
* First 68 lines of lib.rs.
* Declaration of the Kernel struct (without its data elements).
* impl of Kernel struct with headers of public methods.
  * They will all be unimplemented!().
-->

Here is a screenshot of how the Cooperative Multitasking Kernel looks:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/ coop_os_four_procs.png" width=500>

In this screenshot:
* Process `F1` has completed. Its result is displayed, and the user can select to run
  a new process in that space.
* Processes `F2` and `F3` are in progress.
* Process `F4` is blocked awaiting user input.
<!--
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
	
## Design

One instance of each game in progress will be stored in an array. I recommend
using `enum` types to represent both the possible game choices as well as 
the games in progress. Here are the two `enum` types I used in my solution
that you are welcome to use in yours:

	const TASK_MGR_HEADER: usize = 3;
	const MAX_NUM_PROCESSES: usize = BUFFER_HEIGHT - TASK_MGR_HEADER;

	#[derive(Copy,Clone,Eq,PartialEq,Debug)]
	#[repr(u8)]
	enum GameChoice {
		GhostHunter, Tracer, Letters, SpaceInvaders, Chicken, Burnett, Hodgins
	}

	const GAME_CHOICES: [GameChoice; NUM_GAMES] = [GameChoice::Tracer, GameChoice::Letters, GameChoice::GhostHunter, GameChoice::Burnett, GameChoice::Chicken, GameChoice::Hodgins, GameChoice::SpaceInvaders];
	const NUM_GAMES: usize = 7;

	impl GameChoice {
		fn start(&self) -> Process {
			match self {
				GameChoice::GhostHunter => Process::GhostHunter(GhostHunterGame::new()),
				GameChoice::Tracer => Process::Tracer(TracerGame::new()),
				GameChoice::Letters => Process::Letters(LetterMover::new()),
				GameChoice::SpaceInvaders => Process::SpaceInvaders(SpaceInvadersGame::new()),
				GameChoice::Chicken => Process::Chicken(Game::new()),
				GameChoice::Burnett => Process::Burnett(nom_noms::LetterMover::new()),
				GameChoice::Hodgins => Process::Hodgins(MainGame::new())
			}
		}

		fn name(&self) -> &'static str {
			match self {
				GameChoice::GhostHunter => "Ghost Hunter",
				GameChoice::Tracer => "Tracer",
				GameChoice::Letters => "Letter Mover",
				GameChoice::SpaceInvaders => "Space Invaders",
				GameChoice::Chicken => "Chicken Invaders",
				GameChoice::Burnett => "Daniel's Game",
				GameChoice::Hodgins => "Snake"
			}
		}
	}
	
	#[derive(Copy,Clone,Debug,Eq,PartialEq)]
	enum Process {
		GhostHunter(ghost_hunter::MainGame),
		Tracer(TracerGame),
		Letters(LetterMover),
		SpaceInvaders(SpaceInvadersGame),
		Chicken(Game),
		Burnett(nom_noms::LetterMover),
		Hodgins(baremetal_snake::MainGame)
	}

	impl Process {
		fn tick(&mut self) {
			match self {
				Process::GhostHunter(game) => ghost_hunter::tick(game),
				Process::Tracer(game) => game.tick(),
				Process::Letters(game) => game.tick(),
				Process::SpaceInvaders(game) => baremetal_game::tick(game),
				Process::Chicken(game) => game.tick(),
				Process::Burnett(game) => game.tick(),
				Process::Hodgins(game) => baremetal_snake::tick(game)
			}
		}

		fn key(&mut self, key: DecodedKey) {
			match self {
				Process::GhostHunter(game) => game.key(key),
				Process::Tracer(game) => game.key(key),
				Process::Letters(game) => game.key(key),
				Process::SpaceInvaders(game) => game.key(key),
				Process::Chicken(game) => game.key(key),
				Process::Burnett(game) => game.key(key),
				Process::Hodgins(game) => game.key(key)
			}
		}
	}
	
## Other configuration issues

To include the other projects from GitHub in your project, add these lines to
`Cargo.toml`:

	ghost_hunter = {git = "https://github.com/gjf2a/ghost_hunter"}
	bare_metal_tracer = {git = "https://github.com/gjf2a/bare_metal_tracer"}
	pluggable_interrupt_template = {git = "https://github.com/gjf2a/pluggable_interrupt_template"}
	baremetal_game = {git = "https://github.com/scgaskins/baremetal_game"}
	chicken_invaders = {git = "https://github.com/juliebdick/chicken_invaders"}
	nom_noms = {git = "https://github.com/cally-cmd/nom_noms"}
	baremetal_snake = {git = "https://github.com/Haedge/baremetal_snake"}
	
To import them into your source file:

	use ghost_hunter::GhostHunterGame;
	use bare_metal_tracer::TracerGame;
	use pluggable_interrupt_template::LetterMover;
	use baremetal_game::game_core::SpaceInvadersGame;
	use chicken_invaders::Game;
	use baremetal_snake::MainGame;
-->
## Submissions
* Create a **private** GitHub repository for your cooperative kernel.
* Paste the repository URL into your Teams channel.

## Assessment
* **Complete**: Meets all requirements given above.
* **Partial**: Sincere attempt to meet requirements, but incomplete in some way.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).