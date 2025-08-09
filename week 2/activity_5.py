#Week 2 - Activity 5: Develop a project to work with Strings
#Develop a project using class and methods to get a sentence from user input and find the number of words in it.




class WordCounter:
    def count_words(self,sentence):
        words=sentence.split() # Split the sentence into words using space as the separator
        return len(words)
    
sentence=input("Enter a sentence:")
counter=WordCounter()
word_count=counter.count_words(sentence)# Call the method to count words and store the result
print("Number od words", word_count)
