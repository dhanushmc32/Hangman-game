# Hangman Game

A simple console-based Hangman game implemented in Python. The player has 6 lives to guess the correct word, letter by letter. If the player guesses all the letters correctly before running out of lives, they win. Otherwise, they lose, and the stick figure is completed.

## Features
- Random word selection from a predefined list of words.
- Lives decrease with each wrong guess, showing the progression of a Hangman stick figure.
- The game ends either when the player guesses the word or runs out of lives.

## Gameplay

- The game randomly chooses a word from the list `["apple", "beautiful", "potato"]`.
- The player enters one letter at a time to try and guess the word.
- Each correct guess reveals the letter(s) in the hidden word.
- Each incorrect guess reduces the number of lives by one, showing a new stage of the Hangman figure.
- The player wins if they guess the entire word before running out of lives.
- The player loses if they run out of lives without guessing the word.

## Setup and Running the Game

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/hangman-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hangman-game
    ```
3. Run the script:
    ```bash
    python hangman_game.py
    ```

## Files
- `hangman_game.py`: The main Python script that contains the game logic.
- `hangman_stages.py`: A Python file that contains the stages of the Hangman stick figure.

## Example

