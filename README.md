# 🧠 Quiz Game

A console-based multiple-choice quiz game that tests your general knowledge in a fun and interactive way.

## 📜 Description

This Python project presents users with a series of multiple-choice questions. The player inputs their guesses, and the game keeps track of correct and incorrect answers. The final score is displayed at the end.

## 🚀 How to Run

```bash
python 1_quiz_game.py
```

## ✅ Features

- Multiple-choice format
- Real-time feedback (correct/wrong)
- Score calculation and display
- Option to replay

## 🛠 Requirements

This project uses only Python's built-in libraries — no external dependencies required.

## 💡 Future Improvements

- Add question categories or difficulty levels
- Load questions from a file or API
- GUI version using Tkinter

----

# 🎯 Number Guessing Game

A fun and simple Python mini project where the computer randomly selects a number between 1 and 100, and your goal is to guess it.

## 📋 Features

- Random number generated between 1 and 100
- Unlimited attempts
- Feedback whether your guess is too high or too low
- Option to quit anytime by typing `Quit`
- Tracks number of guesses

## ▶️ How to Run

```bash
python 2_number_guessing_game.py
```

----

# ✊🖐✌ Rock Paper Scissors

A simple Python game where you play Rock, Paper, Scissors against the computer.

## 🕹 How to Play

- Type `rock`, `paper`, or `scissors` when prompted.
- The computer randomly picks one too.
- You win, lose, or draw based on the usual game rules.
- Type `no` when asked to quit.

## ▶️ Run the Game

```bash
python 3_rock_paper_scissor.py
```

----

# 🗺️ Choose Your Own Adventure Game

A beginner-friendly, text-based adventure game built in Python. The player makes choices that lead to different outcomes — some good, some fatal!

## 📜 Description

In this game, you play as a traveler exploring unknown paths. You'll encounter rivers, bridges, strangers, and choices that determine your fate. A great way to practice Python conditionals and user input handling.

## ▶️ How to Run

```bash
python 4_choose_your_own_adventure.py
```

## ✅ Features

- Interactive decision-making
- Branching story paths
- Multiple endings (win/lose)
- Simple and beginner-friendly code

## 💡 Future Ideas

- Add scoring or a "health" system
- Include more complex story arcs or side quests
- Add ASCII art or sound effects
- Convert into a GUI using Tkinter

----

# 🖥️ GUI Password Manager

A password manager with a graphical user interface (GUI) built using Tkinter. Encrypts and stores passwords locally using the `cryptography` library.

## ▶️ How to Run

```bash
pip install cryptography
python 5_password_manager.py
```

## ✅ Features

- Secure password storage with encryption
- Add/view functionality in a simple GUI
- Uses Fernet (symmetric encryption)
- Auto-generates a key if not found

## 💡 Future Ideas

- Add master password
- Edit/delete stored passwords
- Export/import functionality

----
# 🎲 Pig Dice Game (Optimized)

A competitive dice game where players race to reach a target score (20). The winner is the one who reaches it with the fewest number of dice rolls.

## ▶️ How to Run

```bash
python 6_pig.py
```
## ✅ Features

- 2 to 4 players
- Re-roll until player holds or rolls a 1
- Tracks how many times each player rolls
- Winner is chosen based on fewest rolls (and highest score in case of tie)

## 💡 Future Ideas

- Add GUI with Tkinter
- Show leaderboard of roll counts
- Allow setting target score dynamically

 ----

  # ✍️ Mad Libs Generator (Enhanced)

A fun and interactive Python project where users fill in blanks in a story by providing words like nouns, verbs, adjectives, etc. The story template is read from a file, and users can generate multiple versions!

---

## ▶️ How to Run

Make sure a file named `story` is in the same folder. It should contain words in `{}` brackets (e.g., `{noun}`, `{verb}`).

Then run:

```bash
python 7_madlibs_generator.py
```
## ✅ Features

- Reads template from external file
- Automatically detects all {placeholder} fields
- Prompts user for each word
- Ensures input is not empty
- Loops for multiple plays
- Optionally saves the generated story to madlib_output.txt

## Example of a story file

Today I went to the {place}. I saw a {adjective} {noun} jumping over a {noun}.
Then I {verb_past_tense} all the way home!

## 💡 Future Improvements

- Allow users to load from multiple templates
- Add support for random word suggestions
- Convert to a web or GUI version

----

 # 🧮 Timed Math Challenge (GUI)
 
A fun and interactive GUI-based math quiz game that challenges users with 10 randomly generated arithmetic problems (addition, subtraction, multiplication). Built with Python and Tkinter.

---

▶️ How to Run
Make sure you have Python installed.

```bash
python 8_Timed_math_challenge.py
```

## ✅ Features

- Clean and user-friendly Tkinter GUI
- 10 math problems using +, -, and *
- Input answer and press Enter to submit
- Tracks number of correct answers
- Displays total and average time at the end
- “Restart” button to play again instantly

## 💡 Future Ideas

- Add difficulty levels (easy, medium, hard)
- Include division and exponent operations
- Maintain a high score leaderboard
- Add background music or timer sounds
- Create a web-based version with Flask or Django

----

# 🎰 Slot Machine Game in Python

This is a simple command-line based **Slot Machine Game** written in Python. It allows players to deposit money, choose the number of lines to bet on, place a bet per line, spin a 3x3 slot machine, and win money based on matching symbols across lines.


## ▶️ How to Run

Make sure you have Python installed (Python 3.x recommended).

1. Save the code in a Python file, e.g., `slot_machine.py`
2. Open your terminal or command prompt
3. Run the game:

```bash
python slot_machine.py
```

## ✅ Features

- Deposit and track balance
- Bet on 1 to 3 horizontal lines
- Randomly generate slot spins
- Match symbols to win money
- Adjustable bet amounts with min and max limits
- Displays winnings and winning lines
- Balance update after each spin

## 💡 Future Ideas

- Add diagonal or vertical winning logic
- Improve symbol randomization with better probability control
- Add a GUI using Tkinter or PyQt
- Save balance to a file or database for session persistence

  ----

  
 # 🐢 Turtle Racing Game
A colorful, animated turtle racing game built using Python's turtle graphics module. Players can select the number of racers, watch them speed across the screen, and cheer for their favorite turtle!


## ▶️ How to Run
Make sure you have Python installed (Python 3.x recommended).
``` bash
python 10_turle_racing.py
```

## ✅ Features

- Choose between 2 to 10 racers
- Randomly selected turtle colors
- Fully animated race using Turtle graphics
- Winner announced in the console
- Beginner-friendly code with easy customization


## 💡 Future Ideas

- Add a GUI start menu with race options
- Include cheering sound effects
- Track multiple race stats and leaderboard
- Let players bet on a turtle before the race
- Display winning time or race duration

----

# ⌨️ WPM Typing Test (Terminal)
A terminal-based typing speed test application using the curses module. The program measures your words per minute (WPM) by comparing your typed text to a randomly chosen sentence.

## ▶️ How to Run
Make sure you have Python installed.
``` bash
python 11_wpm_typing_test.py
```
🔴 On Windows (not directly supported):
Install windows-curses first: 
``` bash
pip install windows-curses
```

#📋 Required File
You must have a file named:

``` bash
wpm_text_file.txt
```
...in the same folder, containing lines like:

## ✅ Features

- Terminal UI with color-coded feedback
- Calculates and displays WPM in real-time
- Random sentence is loaded each round
- Replays the test automatically until ESC is pressed
- Gracefully handles missing file with a fallback sentence

## 💡 Future Ideas

- Save high scores
- Add difficulty levels (short/long sentences)
- Support timed challenges (e.g., 60 seconds typing mode)
- Export results to a file

----

# ⏰ Alarm Timer with Sound (12_timer.py)

A simple Python script that plays an alarm sound after a user-defined countdown. Ideal for short reminders or personal timeboxing.

---

## 📜 Description

This lightweight script prompts the user to enter a countdown time in seconds. After counting down to zero, it plays an alarm sound using the `pygame` library. It’s a simple, terminal-based tool that helps with personal productivity or study intervals.

---

## ▶️ How to Run

1. Ensure you have Python installed (Python 3.x recommended).
2. Place an audio file named `alaram.wav` in the same directory.
3. Run the script:

```bash
python 12_timer.py
```

## ✅ Features

- User input for custom countdown duration
- Real-time countdown in the terminal
- Plays an alarm (alaram.wav) at the end
- Keeps the program running until the sound finishes

## 📦 Requirements
Install the required library:

``` bash
pip install pygame
```
Make sure the file alaram.wav is placed in the same folder as 12_timer.py.

## 💡 Future Improvements

- GUI version using tkinter
- Option to choose alarm sound dynamically
- Support for hh:mm:ss input format
- Add pause/resume functionality




## 📜 License

This project is open-source under the MIT License.
