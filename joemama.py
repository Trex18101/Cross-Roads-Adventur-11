import random
# Define a list of responses for Joe Mama jokes
responses = [
 "Who is Joe Mama?",
 "Joe Mama is a legend!",
 "Joe Mama has been around forever.",
 "Everyone knows about Joe Mama!",
 "You really don't know who Joe Mama is?",
 "Sorry, I can't reveal the identity of Joe Mama.",
 "Joe Mama is the man!",
 "Joe Mama is a mystery to most people.",
 "I can't believe you don't know Joe Mama.",
]


# Define the main function
def play_game():
	print("Welcome to the Joe Mama game!")
	print("Try to guess who Joe Mama is by answering some trivia questions.")
	print("Type 'quit' to exit the game at any time.")

	# Loop through the questions until the user types "quit"
	while True:
		# Generate a random question from the list
		question = random.choice([
		 "What is Joe Mama's favorite color?", "What is Joe Mama's favorite food?",
		 "What is Joe Mama's favorite hobby?"
		])

		# Prompt the user to answer the question
		answer = input(question + " ")

		# Check if the user wants to quit the game
		if answer.lower() == "quit":
			print("Thanks for playing!")
			break

		# Generate a random response to the answer
		response = random.choice(responses)

		# Print the response
		print(response)


# Call the main function to start the game
play_game()
