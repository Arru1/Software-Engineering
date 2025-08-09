import random

def word_guessing_game():
    words = ['python', 'java', 'programming', 'developer']
    word = random.choice(words).lower()  # Select a random word and convert to lowercase
    blanks = ['_'] * len(word)  # Create blanks for the word
    lives = 10  # Number of lives (increased to allow more guesses)
    
    print("Welcome to the Word Guessing Game!")
    
    while lives > 0:
        print("\nCurrent word:", ' '.join(blanks))  # Display the current state of the word
        print(f"Lives remaining: {lives}")  # Display remaining lives
        
        guess = input("Guess a letter or the full word: ").lower()  # Get the user input
        
        # If the guess is a single letter
        if len(guess) == 1:
            if not guess.isalpha():  # Ensure it's a valid letter
                print("Please enter only one letter.")
                continue
            
            # Check if the guessed letter is in the word
            if guess in word:
                print(f"Good guess! The letter '{guess}' is in the word.")
                for i in range(len(word)):
                    if word[i] == guess:
                        blanks[i] = guess
            else:
                print(f"Oops! The letter '{guess}' is not in the word.")
                lives -= 1  # Decrease lives for incorrect guess
        
        # If the guess is a full word
        elif len(guess) == len(word):
            if guess == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
            else:
                print(f"Oops! The word '{guess}' is incorrect.")
                lives -= 1
        
        else:
            print("Invalid input! Please guess a letter or the full word.")
        
        # Check if the word is completely guessed
        if '_' not in blanks:
            print(f"Congratulations! You guessed the word: {''.join(blanks)}")
            break
        
        # Check if the player has run out of lives
        if lives == 0:
            print(f"Game over! The word was: {word}")


word_guessing_game()
