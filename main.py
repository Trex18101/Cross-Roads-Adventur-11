import random
import features
from clippy import Clippy
import time
from icecream import ic

def read_all_names() -> None:
	'''
 	Gets every first, middle and last name stored in it's corresponding text file
  	Then it puts the list into a variable.
 	'''
	global first_names
	global middle_names
	global last_names
	#opens first.txt and stores them in a list
	with open('text_files/names/first.txt') as first:
		first_names = first.read().splitlines()

	#opens middle.txt and stores them in a list
	with open('text_files/names/middle.txt') as middle:
		middle_names = middle.read().splitlines()

	#opens last.txt and stores them in a list
	with open('text_files/names/last.txt') as last:
		last_names = last.read().splitlines()


def generate_random_name() -> str:
	'''
 	Generates a random name
  	'''
	# first names
	first_name_index = random.randint(0, len(first_names))
	first_name = first_names[first_name_index]

	# middle names
	if random.randint(0, 100) <= 80:
		middle_name_index = random.randint(0, len(middle_names))
		middle_name = middle_names[middle_name_index]
	else:
		middle_name = ''

	# last names
	last_name_index = random.randint(0, len(last_names))
	last_name = last_names[last_name_index]

	# return name
	if middle_name == '':
		return first_name + ' ' + last_name
	else:
		return first_name + ' ' + middle_name + ' ' + last_name


#opens clippy.txt and loads ur guide named clippy (we hate you windows)
with open('text_files/art/clippy.txt') as clip:
	global clippy_art
	clippy_art = clip.read()

read_all_names()
clippy_name = generate_random_name()
clippy = Clippy(clippy_name, clippy_art)
clippy.show()

features.slow_print('Hello!')
features.slow_print('I\'m your guide!')
features.slow_print('It looks like you\'re writing a letter.')
features.slow_input('Do you need some help?')
