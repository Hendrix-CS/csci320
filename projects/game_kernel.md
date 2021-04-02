---
layout: work
type: Project
num: 9
worktitle: Game Kernel
---

## Overview

Arcade consoles allow a user to select a game to play, play it, and when it
ends, select another game. In this project, you will implement a Game Kernel
that enables this functionality, plus a bit more. Specifically, your Game
Kernel will allow users to suspend a game in progress, resume a suspended game,
and even have multiple instances of the same game in progress at once.

Here is a screenshot of how the Game Kernel looks:

<img src="https://hendrix-cs.github.io{{site.baseurl}}/assets/images/Game_Kernel_In_Progress.PNG" width=500>

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
	
## Submissions
* Create a **private** GitHub repository for your webserver program.
* Paste the repository URL into your Teams channel.

## Assessment
* **Complete**: Meets all requirements given above.
* **Partial**: Sincere attempt to meet requirements, but incomplete in some way.

## Acknowledgement

This assignment was adapted from [materials](https://os.phil-opp.com/) developed by 
[Philipp Oppermann](https://github.com/phil-opp).