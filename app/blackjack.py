'''defines the Blackjack class'''

from .player import Player
from .deck import Deck
from .input_handling import match_yes, next_player, press_return

class Blackjack():
	'''the class that keeps track of gameplay

	kw args:
		num_players -- the number of players, an integer between 2 and 4

		names -- an array of player names

	instance variables:
		deck -- a Deck object

		players -- a list of Player objects

	methods:
	'''
	def __init__(self, num_players, names=[]):
		'''initializes the Blackjack class

		kw args:
			num_players -- the number of players, an integer between 2 and 4

			names -- an array of player names

		instance variables:
			deck -- a Deck object

			players -- a list of Player objects
		'''
		self.deck = Deck()
		self.players = []

		# record player names
		for player in range(num_players):
			if names:
				self.players.append(Player(self.deck, \
					names[player]))
			else:
				self.players.append(Player(self.deck, \
					input("What's your name, player {}?\n".format(player + 1))))

	def unbroken(self):
		'''
		returns a list of players who are 'unbroken' (i.e. the sum
		of their hand is below 22)
		'''
		return list(filter(lambda player: player.sum_hand() <= 21, self.players))

	def start_round(self):
		'''starts a round of Blackjack'''
		# print each player's hand
		for player in self.players:
			next_player(player)
			player.print_hand()
			press_return()

		# move to next turn
		self.next_turn()

	def next_turn(self):
		'''runs the next turn of blackjack game'''
		# iterate through players
		for player in self.players:
			if player.cont and len(self.unbroken()) > 1:
				next_player(player)
				player.print_hand()

				# queries the player
				if match_yes("Would you like to draw another card, {}?".format(player.name)):
					player.draw()
					player.print_hand()

					# checks if player is "broken"
					if player.sum_hand() > 21:
						print("You're out!")
						player.cont = False
				else:
					player.cont = False

				press_return()

		# checks if another turn is necessary
		if any(map(lambda player: player.cont, self.players)) and len(self.unbroken()) > 1:
			self.next_turn()

		# ends game
		else:
			self.end()

	def end(self):
		'''finishes the blackjack game'''
		# find the winner
		winner = max(self.unbroken(), key = lambda player: player.sum_hand())
		# print congratulations
		print("Congratulations, {}! With a score of {}, you've won!".format(winner.name, winner.sum_hand()))

		# queries the user if they would like to play again
		if match_yes("Would you like to play again?"):
			game = Blackjack(len(self.players), names = list(map(lambda player: player.name, self.players)))
			game.start_round()
