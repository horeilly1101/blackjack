'''contains functions that deal with input handling and user interface

functions:
	match_yes -- returns the matching of the input to a regular expression that
		evaluates to a lone-standing "y"

	match_num -- returns the matching of the input to a regular expression that
		evaluates to a lone-standing integer

	get_num_players -- returns an integer between 2 and 4 from the user

	next_player -- ticks for 3 seconds between turns

	press_return -- queries the user to press return
'''

import re
from player import Player
import time

def match_yes(input_string):
	'''
	returns the matching of the input to a regular expression that
	evaluates to a lone-standing "y"

	kw args:
		input_string -- the string the user will see, should be a
			yes or no question
	'''
	# compile the regular expression
	yes_pattern = re.compile("\\by\\b")

	# searches the user's input for the regular expression
	return re.search(yes_pattern, input(input_string + " (y/n)\n"))

def match_num(input_string):
	'''
	returns the matching of the input to a regular expression that
	evaluates to a lone-standing integer

	kw args:
		input_string -- the string the user will see, should be answered with
			an integer
	'''
	# compile the regular expression
	num_pattern = re.compile("\\b[0-9][1-9]*\\b")

	# searches the user's input for the regular expression
	return re.search(num_pattern, input(input_string + "\n"))

def get_num_players():
	'''returns an integer between 2 and 4 from the user'''
	try:
		# queries user for number
		num_players = int(match_num("How many players? (2-4)").group(0))
		# checks that number is in correct interval
		if num_players >= 2 and num_players <=4:
			return num_players
		else:
			# queries the user again
			print("Please input an integer between 2 and 4.")
			get_num_players()
	except:
		# queries the user again
		print("Please input an integer between 2 and 4.")
		get_num_players()

def next_player(player):
	'''ticks for 3 seconds between turns

	kw args:
		player --  a Player object
	'''
	print()
	for i in range(3, 0, -1):
		# prints time until next turn
		print("{}'s turn in {}".format(player.name, i))
		# pauses the program for a second
		time.sleep(1)

	# skips 25 lines
	print("\n" * 25)

def press_return():
	'''queries the user to press return'''
	input("Press return to continue.")
	# skips 25 lines
	print("\n" * 25)
