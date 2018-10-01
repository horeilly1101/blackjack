# blackjack
Rules: Get as close to 21 as you can without going over. The player without the highest number less than 21 wins.

## My implementation
- Allows 2 - 4 players
- Entirely console-based
- Allows a 3-second "grace period" between turns for players to pass the computer amongst themselves
- Is pretty fun to play with friends

## Design Designs
- I didn't use any "crazy" libraries, so the entire game can be run as long as you have the latest version of Python 3 installed.
- **functools** allows me to use the "reduce" function, which greatly simplifies the code.
