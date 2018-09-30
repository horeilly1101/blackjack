from card import Card
from random import shuffle

class Deck():
	def __init__(self):
		'''initialize Deck object

		instance variables:
			_deck -- a randomly shuffled list of distinct Card objects
		'''
		# create and shuffle list of 52 numbers
		deck = [i for i in range(52)]
		shuffle(deck)

		# convert numbers to Card objects
		self._deck = list(map(lambda card: Card(card), deck))

	def __str__(self):
		return str(list(map(lambda card: str(card), self._deck)))

	def shuffle(self):
		shuffle(self._deck)

	def draw(self):
		return self._deck.pop()
