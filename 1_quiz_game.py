# Define the function to start a new game
def new_game():

    guesses = []  # Initialize an empty list to store user's guesses
    corect_guesses = 0  # Initialize the count of correct guesses
    question_num = 1  # Initialize the question number

    # Loop through each question in the 'questions' dictionary
    for key in questions:
        print("----------------------------------")
        print(key)  # Print the question

        # Print the multiple-choice options for the current question
        for i in options[question_num - 1]:
            print(i)

        # Prompt the user for their guess
        guess = input("Enter (A, B, C, or D):")
        guess = guess.upper()  # Convert the guess to uppercase
        guesses.append(guess)  # Add the guess to the 'guesses' list

        # Check the answer and update the count of correct guesses
        corect_guesses += check_answer(questions.get(key), guess)
        question_num += 1  # Move to the next question
    # Display the final score
    display_score(corect_guesses, guesses)


# Define the function to check if the user's guess is correct
def check_answer(answer, guess):

    # If the guess matches the correct answer
    if answer == guess:
        print("Correct!")
        return 1  # Return 1 for a correct answer
    else:
        print("Wrong!")
        return 0  # Return 0 for an incorrect answer


# Define the function to display the final score
def display_score(correct_guesses, guesses):
    print("----------------------------------")
    print("RESULTS")
    print("----------------------------------")
    print("Answers: ", end="")

    # Print the correct answers
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # Print the user's guesses
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    # Calculate the score as a percentage
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")  # Print the score


# Define the function to ask the user if they want to play again
def play_again():
    response = input("Do you want to play again? (yes/no):")  # Prompt the user
    response = response.upper()  # Convert the response to uppercase
    if response == "YES":  # Check if the response is 'YES'
        return True
    else:
        return False


# Define the dictionary holding the questions and their correct answers
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A",
}

# Define the list of lists, each containing the multiple-choice options for each question
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. Right", "B. Wrong", "C. Sometimes", "D. What EARTH ??"],
]

# Start the initial game
new_game()

# Loop to play again
while play_again():
    new_game()  # Start a new game if the user wants to play again

# Print the goodbye message when the user decides not to play again
print("Byee!! Have a good day")
