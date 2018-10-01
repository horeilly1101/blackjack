'''definition of Card class'''
class Card():
	'''class that keeps track of individual 'cards'

	class variables:
		_royals -- maps integers to "royal" strings

		_suits -- maps integers to "suits"

		_values -- maps "royals" to rank values

	instance variables:
		suit (string) -- the suit of a card

		num (string) -- the "type" of a card

	methods:
		value -- returns the rank value of a card
	'''
	# define royals
	_royals = {
		0 : "Ace",
		1 : "Jack",
		11 : "Queen",
		12 : "King"
	}

	# define suits
	_suits = {
		0 : "SPADES",
		1 : "DIAMONDS",
		2 : "HEARTS",
		3 : "CLUBS"
	}

	# define rank values
	_values = {
		"Ace" : 1,
		"Jack" : 10,
		"Queen" : 10,
		"King" : 10
	}

	def __init__(self, id):
		'''initializes a Card objects

		kw args:
			self -- A Card objects

			id -- an integer in the interval [0, 52)
		'''
		if id >= 0 and id < 52:
			suit, num = divmod(id, 13)
			# assign suit
			self.suit = Card._suits[suit]
			# assign type
			self.num = str(num) if not num in Card._royals else Card._royals[num]
		else:
			raise ValueError("Card 'id' must be an integer in the interval [0, 52)!")

	def __str__(self):
		'''converts Card object to a string

		kw args:
			self -- a Card object
		'''
		return "{} of {}".format(self.num, self.suit)

	def value(self):
		'''returns the 'value' of a Card objects

		kw args:
			self -- a Card object
		'''
		return int(self.num) if not self.num in Card._values else Card._values[self.num]
