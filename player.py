from deck import Deck
from functools import reduce

class Player():
	def __init__(self, deck, name):
		self.name = name
		self.hand = [deck.draw(), deck.draw()]
		self.deck = deck
		self.cont = True

	def draw(self):
		self.hand.append(self.deck.draw())

	def sum_hand(self):
		min_sum = reduce(lambda sum, card: sum + card.value(), self.hand, 0)
		if "Ace" in self.hand and min_sum + 10 <= 21:
			return min_sum + 10
		else:
			return min_sum

	def print_hand(self):
		print("{}'s Hand:".format(self.name))
		for card in self.hand:
			print(" ", card)
		print("")
