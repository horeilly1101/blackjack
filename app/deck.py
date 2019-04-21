'''definition of Deck class'''

from .card import Card
from random import shuffle

class Deck():
	'''class that keeps track of a "deck" of cards

	instance variables:
		_deck (list<Card>) -- a list of Card objects

	methods:
		draw -- draw a card from the deck
	'''
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
		'''convert Deck object into a string'''
		return str(list(map(lambda card: str(card), self._deck)))

	def draw(self):
		'''pop a card from the deck'''
		return self._deck.pop()
