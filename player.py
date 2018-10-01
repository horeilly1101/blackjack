'''defines player class'''

from deck import Deck
from functools import reduce

class Player():
	'''defines class to keep track of player-specific states

	instance variables:
		name (string) -- name of the player

		hand (list<Card>) -- the cards in the players "hand"

		deck -- the deck the player is using

		cont (boolean) -- whether or not the player may still draw a card
	'''
	def __init__(self, deck, name):
		'''initializes the Card object

		kw args:
			deck -- the deck the player is using

			name (string) -- name of the player


		instance variables:
			name (string) -- name of the player

			hand (list<Card>) -- the cards in the players "hand"

			deck -- the deck the player is using

			cont (boolean) -- whether or not the player may still draw a card
		'''
		self.name = name
		# starts the player with two cards
		self.hand = [deck.draw(), deck.draw()]
		self.deck = deck
		self.cont = True

	def draw(self):
		'''draws a card'''
		self.hand.append(self.deck.draw())

	def sum_hand(self):
		'''returns the sum of the values of the cards in the player's hand'''
		# calculate minimun sum
		min_sum = reduce(lambda sum, card: sum + card.value(), self.hand, 0)
		# determines if any "Ace" cards are helpful
		if "Ace" in self.hand and min_sum + 10 <= 21:
			return min_sum + 10
		else:
			return min_sum

	def print_hand(self):
		'''prints all the cards in the player's hand'''
		print("\n{}'s Hand:".format(self.name))
		for card in self.hand:
			print(" ", card)
		print()
