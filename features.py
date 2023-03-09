import sys, os, time

def slow_print(text):
	'''
 	Simulates typewriting
  	'''
	for char in text + '\n':
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.5)

def slow_input(text):
	'''
 	Simulates typewriting input
  	'''
	for char in text + '\n':
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)

	input()

def clear():
	if(os.name == 'posix'):
	   os.system('clear')
	else:
	   os.system('cls')