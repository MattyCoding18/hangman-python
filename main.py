import random
from hangman_words import word_list
from hangman_art import stages, logo

# Game setup
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
correct_letters = []
game_over = False

# Display the logo at the start
print(logo)

# Create initial display with underscores
display = "_" * word_length
print(f"Word to guess: {display}")

# Main game loop
while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You have already guessed '{guess}'. Try another letter.")
        continue  # Skip to next iteration

    # Update display for correct guesses
    updated_display = ""
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            updated_display += letter
            correct_letters.append(guess)
        else:
            updated_display += display[index]  # Preserve previous correct letters

    display = updated_display
    print(f"Word to guess: {display}")

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\n*********************** IT WAS '{chosen_word}'! YOU LOSE **********************")

    # Check for win condition
    if "_" not in display:
        game_over = True
        print("\n**************************** YOU WIN! ****************************")

    # Display the hangman stage
    print(stages[lives])
