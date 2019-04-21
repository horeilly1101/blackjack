'''runs the blackjack game!'''

from app.input_handling import match_yes, get_num_players
from app.blackjack import Blackjack

if __name__ == "__main__":
	print("\nWelcome to blackjack!")

	if match_yes("Would you like to play Blackjack?"):
		# starts game
		game = Blackjack(get_num_players())
		game.start_round()

	print("\nHave a great day!")
