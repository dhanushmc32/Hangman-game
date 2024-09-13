import random
import hangman_stages

# List of words to choose from
word_list = ["apple", "beautiful", "potato"]

# Initial number of lives
lives = 6

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)  # For debugging purposes, the chosen word is printed (remove for actual gameplay)

# Create a display list where guessed letters are shown, initially filled with underscores
display = []
for i in range(len(chosen_word)):
    display += '_'  # Each underscore represents an unguessed letter

# Variable to keep track of whether the game is over
game_over = False

# Main game loop
while not game_over:
    # Ask the player to input a guessed letter
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter  # Replace underscore with the correctly guessed letter

    # Print the current state of the word with guessed letters
    print(display)

    # If the guessed letter is not in the chosen word, reduce lives
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True  # End the game if no lives are left
            print("You lose!!")  # Inform the player they lost

    # Check if the player has guessed all letters
    if '_' not in display:
        game_over = True  # End the game if all letters are guessed
        print("You win!!")  # Inform the player they won

    # Print the current stage of the hangman depending on the number of lives left
    print(hangman_stages.stages[lives])
