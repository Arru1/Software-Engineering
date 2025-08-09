import random

class WordGuessingGame:
    def __init__(self):
        self.words = ['python', 'java', 'programming', 'developer']
        self.word = random.choice(self.words).lower()  # Random word
        self.blanks = ['_'] * len(self.word)  # Blanks for the word
        self.lives = 10  # Number of lives

    def display(self):
        # Display the current word with blanks and remaining lives
        print("Current word:", ' '.join(self.blanks))  
        print(f"Lives remaining: {self.lives}")

    def guess_letter(self, guess):
        if len(guess) != 1 or not guess.isalpha():  # Validate guess
            print("Please enter only one letter.")
            return False
        if guess in self.word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.blanks[i] = guess
            return True
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            self.lives -= 1  # Decrease lives for incorrect guess
            return False

    def is_game_over(self):
        # Check if word is completely guessed or lives are zero
        if '_' not in self.blanks:
            print(f"Congratulations! You guessed the word: {''.join(self.blanks)}")
            return True
        if self.lives <= 0:
            print(f"Game over! The word was: {self.word}")
            return True
        return False

def main():
    game = WordGuessingGame()
    print("Welcome to the Word Guessing Game!")
    
    while not game.is_game_over():
        game.display()
        guess = input("Guess a letter: ").lower()  # Get user input
        if not game.guess_letter(guess):
            continue  # If invalid guess, loop again

if __name__ == "__main__":
    main()
