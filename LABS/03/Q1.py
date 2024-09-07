# Write a Python program that reads a text file, counts the number of characters in it, and prints the total word count. Handle all possible exceptions as well.

file_name = input("Enter file name: ")
try:
    with open(f"{file_name}.txt", 'r') as file:

        content = file.read()

    
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except IOError:
    print("Error occurred while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print(content)
    print("Char count: ", len(content))
    print("Word count: ", len(content.split()))
