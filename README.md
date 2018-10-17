# blackjack
Rules: Get as close to 21 as you can without going over. The player without the highest number less than 22 wins.

<img src="blackjack_ui.png" alt="user interface" width="200"/>

## My implementation
- Allows 2 - 4 players
- Is entirely console-based
- Allows a 3-second "grace period" between turns for players to pass the computer amongst themselves
- Is pretty fun to play with friends

## Design designs
- I didn't use any "crazy" libraries, so the entire game can be run as long as you have the latest version of Python 3 installed. But these are the standard libraries I used:
  - *functools* allows me to use the "reduce" function, which greatly simplifies the code.
  - *re* allows me to use regular expression matching to simplify the entire process of parsing user input.
  - *random* allows me to randomly permute the deck of cards, ensuring that the game is as close to real life as possible.
  - *time* allows me to momentarily pause the program between turns.
- The implementation of the game was pretty simple, so I didn't find it necessary to use data structures more complicated than arrays or maps.
- I decided to used the "mutation style" of object-oriented programming, even though this is often frowned upon, because it made it much easier to ensure that the same deck was used throughout the game.  I consider this to be a crucial feature of a card game.

## How to run on mac OS
- Ensure that the latest version of Python 3 is installed.
- Navigate to the directory where the files are stored. (You should also make sure that all of the files are there, in the same directory.)
- Run `python3 play.py` in the terminal.
