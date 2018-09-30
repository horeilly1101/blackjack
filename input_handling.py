import re
from player import Player
import time

def match_yes(input_string):
	yes_pattern = re.compile("\\by\\b")
	return re.search(yes_pattern, input(input_string + " (y/n)\n"))

def match_num(input_string):
	num_pattern = re.compile("\\b[0-9][1-9]*\\b")
	return re.search(num_pattern, input(input_string + "\n"))

def get_num_players():
	try:
		num_players = int(match_num("How many players? (2-4)").group(0))
		if num_players >= 2 and num_players <=4:
			return num_players
		else:
			print("Please input an integer between 2 and 4.")
			get_num_players()
	except:
		print("Please input an integer between 2 and 4.")
		get_num_players()

def next_player(player):
	i = 3
	print("")
	while i > 0:
		print("{}'s turn in {}".format(player.name, i))
		i -= 1
		time.sleep(1)
	print("\n" * 25)

def press_return():
	input("Press return to continue.")
	print("\n" * 25)
