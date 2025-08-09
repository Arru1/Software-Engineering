import random

def word_guessing_game():
    words = ['python', 'java', 'programming', 'developer']
    word = random.choice(words).lower()  # Select a random word and convert to lowercase
    blanks = ['_'] * len(word)  # Create blanks for the word
    lives = 4  # Number of lives
    
    print("Welcome to the Word Guessing Game!")
    
    while lives > 0:
        print("Current word:", ' '.join(blanks))  # Display the current state of the word
        print(f"Lives remaining: {lives}")  # Display remaining lives
        
        guess = input("Guess a letter: ").lower()  # Get the user input and convert to lowercase
        
        if len(guess) != 1 or not guess.isalpha():  # Ensure it's a valid letter
            print("Please enter only one letter.")
            continue
        
        # Check if the guessed letter is in the word (case-insensitive)
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            lives -= 1  # Decrease lives for incorrect guess
            
        # Check if the word is completely guessed
        if '_' not in blanks:
            print(f"Congratulations! You guessed the word: {''.join(blanks)}")
            break
        
        # Check if the player has run out of lives
        if lives == 0:
            print(f"Game over! The word was: {word}")


word_guessing_game()
