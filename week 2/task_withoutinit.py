class StringManipulator:
    def find_character(self, text, char):
        return text.find(char)

    def length(self, text):
        return len(text)

    def upper(self, text):
        return text.upper()


if __name__ == '__main__':
    text = input("Enter a string: ")
    char = input("Enter a character to find: ")

    name = StringManipulator()

    index = name.find_character(text, char)
    print(f'\nThe text is: "{text}"')
    print(f'\nThe index of "{char}" is: {index}')
    print(f'The length of "{text}" is: {name.length(text)}')
    print(f'\nThe uppercase of "{text}" is: {name.upper(text)}')
