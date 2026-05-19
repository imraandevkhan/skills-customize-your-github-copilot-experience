
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman-style word-guessing game using Python strings, loops, conditionals, and user input. Practice program flow by tracking guesses, showing progress, and ending the game with win/lose messages.

## 📝 Tasks

### 🛠️ Build the Hangman Game Core

#### Description
Create the main game loop that selects a random word and allows the player to guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Prompt the user to guess one letter at a time using `input()`.
- Show the current word progress using underscores for unknown letters, for example: `_ a _ g m a n`.
- Track and display the number of incorrect guesses remaining.
- End the game when the player guesses the full word or uses all attempts.

### 🛠️ Display Feedback and Win/Lose Results

#### Description
Add feedback for each guess and clearly show the final game result.

#### Requirements
Completed program should:

- Inform the player whether each guessed letter is correct or incorrect.
- Prevent repeated guesses from reducing the remaining attempts.
- Display a winning message with the full word when the player succeeds.
- Display a losing message and reveal the word when the player runs out of attempts.
- Example output:
  ```text
  Guess a letter: a
  Correct! _ a _ g m a n
  Guess a letter: e
  Incorrect. Attempts left: 5
  ```