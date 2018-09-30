from player import Player
from deck import Deck
from input_handling import match_yes, next_player, press_return

class Blackjack():
	def __init__(self, num_players, names=[]):
		self.deck = Deck()
		self.players = []
		for player in range(num_players):
			if names:
				self.players.append(Player(self.deck, \
					names[player]))
			else:
				self.players.append(Player(self.deck, \
					input("What's your name, player {}?\n".format(player + 1))))

	def unbroken(self):
		return list(filter(lambda player: player.sum_hand() <= 21, self.players))

	def start_round(self):
		# print hands
		for player in self.players:
			next_player(player)
			player.print_hand()
			press_return()

		# move to next turn
		self.next_turn()

	def next_turn(self):
		for player in self.players:
			if player.cont and len(self.unbroken()) > 1:
				next_player(player)
				player.print_hand()

				if match_yes("Would you like to draw another card, {}?".format(player.name)):
					player.draw()
					player.print_hand()
					if player.sum_hand() > 21:
						print("You're out!")
						player.cont = False
				else:
					player.cont = False

				press_return()

		if any(map(lambda player: player.cont, self.players)) and len(self.unbroken()) > 1:
			self.next_turn()
		else:
			self.end()

	def end(self):
		winner = max(self.unbroken(), key = lambda player: player.sum_hand())
		print("Congratulations, {}! With a score of {}, you've won!".format(winner.name, winner.sum_hand()))
		if match_yes("Would you like to play again?"):
			game = Blackjack(len(self.players), names = list(map(lambda player: player.name, self.players)))
			game.start_round()
