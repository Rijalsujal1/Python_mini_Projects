import random

target = random.randint(1, 100)
# print(target)
guessess = 0
while True:
    user_choice = input("Enter your guess? or Quit(Q): ")
    guessess += 1
    quit = ("Quit").lower()
    if user_choice == quit:
        break
    user_choice = int(user_choice)

    if user_choice == target:
        print("Success: Correct Guess!!")
        break

    elif user_choice < target:
        print("Your number is small")

    else:
        print("Your number is large")

print(f"You guessed the number in {guessess} guesses ")

print("--------Game Over!!!!-----------")

# with open("highscore.txt", "r") as f:
#     highscore = int(f.read())

# if guessess < highscore:
#     print("you have just broken the high score!")
#     with open("highscore", "w") as f:
#         f.write(str(guessess))
