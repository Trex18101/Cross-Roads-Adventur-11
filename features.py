import sys, os, time

def slow_print(text, delay=0.01):
	'''
 	Simulates typewriting
  	'''
	for char in text + '\n':
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)

def slow_input(text, delay=0.01):
	'''
 	Simulates typewriting input
  	'''
	for char in text + '\n':
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)

	input()

def clear():
	if(os.name == 'posix'):
	   os.system('clear')
	else:
	   os.system('cls')