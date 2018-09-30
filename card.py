class Card():
	_royals = {
		0 : "Ace",
		1 : "Jack",
		11 : "Queen",
		12 : "King"
	}

	_suits = {
		0 : "SPADES",
		1 : "DIAMONDS",
		2 : "HEARTS",
		3 : "CLUBS"
	}

	_values = {
		"Ace" : 1,
		"Jack" : 10,
		"Queen" : 10,
		"King" : 10
	}

	def __init__(self, id):
		if id >= 0 and id < 52:
			suit, num = divmod(id, 13)
			self.suit = Card._suits[suit]
			self.num = str(num) if not num in Card._royals else Card._royals[num]
		else:
			raise ValueError("Card 'id' must be an integer in the interval [0, 52)!")

	def __str__(self):
		return "{} of {}".format(self.num, self.suit)

	def value(self):
		return int(self.num) if not self.num in Card._values else Card._values[self.num]
