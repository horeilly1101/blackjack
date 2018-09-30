import re

def match_yes(input_string):
	yes_pattern = re.compile("\\by\\b")
	return re.search(yes_pattern, input(input_string + " (y/n)\n"))

def match_num(input_string):
	num_pattern = re.compile("\\b[0-9][1-9]*\\b")
	return re.search(num_pattern, input(input_string + "\n"))

def get_num_players():
	try:
		return int(match_num("How many players? (1-4)").group(0))
	except:
		print("Please input an integer between 1 and 4.")
		get_num_players()
