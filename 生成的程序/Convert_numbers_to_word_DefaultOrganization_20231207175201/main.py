'''
This is the main file of the numerical to word converter program.
It handles user input and calls the necessary functions to convert the number to words.
'''
from converter import convert_to_words
def main():
    while True:
        number = input("Enter a number to convert (or 'exit' to quit): ")
        if number.lower() == 'exit':
            break
        try:
            number = int(number)
            words = convert_to_words(number)
            print(words)
        except ValueError:
            print("Invalid number entered. Please try again.")
if __name__ == "__main__":
    main()