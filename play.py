from input_handling import match_yes
from blackjack import Blackjack
from input_handling import get_num_players

if __name__ == "__main__":
	print("\nWelcome to blackjack!")

	if match_yes("Would you like to play Blackjack?"):
			game = Blackjack(get_num_players())
			game.start_round()

	print("Have a great day!")
