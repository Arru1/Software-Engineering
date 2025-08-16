class FileProcessing:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_file(self, content):
        with open(self.filepath, "w") as file:
            file.write(content)

    def read(self):
        with open(self.filepath, "r") as file:
            return file.read()

def main():
    # Create an instance of FileProcessing
    file_processor = FileProcessing("demo.txt")

    # Read from the file
    content = file_processor.read()
    print(content)
    
    # Write to the file
    file_processor.write_file("Hello, this is a simple file!\n")
    
    

if __name__ == "__main__":
    main()
#Week3- Activity 1: Work with .txt file
#Using the attached text file, open, read, and write the complete information for the demo.txt. 
#Share the GitHub link here(with adding the screenshot of the result).

