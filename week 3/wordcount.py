class WordCounter:
    def __init__(self, filepath):
        self.filepath = filepath  # Store the file path
    
    def count_words(self):
            with open(self.filepath, 'r') as file:
                content = file.read()  # Read the entire content of the file
                words = content.split()  # Split the content by spaces into words
                return len(words)  # Return the total number of words
        

def main():
    # Create an instance of WordCounter with the file path
    counter = WordCounter("demo.txt")
    
    # Get the word count
    word_count = counter.count_words()
    
    # Print the result
    print(f"Total number of words in demo.txt: {word_count}")

if __name__ == "__main__":
    main()
