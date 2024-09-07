
#2. Create a program that reads a text file, searches for a specified word or phrase, and replaces
#all occurrences with another word or phrase. Write the modified content back to the file.
# Handle all possible exceptions as well.


file_name = input("Enter the file name: ")
search = input("Enter the word to search for: ")
replace = input("Enter the word to replace it with: ")

try:
    with open(f"{file_name}.txt", 'r') as file:
        content = file.read()

    modified = content.replace(search, replace)

    # Open the file for writing and write the modified content back to the file
    with open(f"{file_name}.txt", 'w') as file:
        file.write(modified)


except FileNotFoundError:
    print(f"The file '{file_name}.txt' was not found.")
except IOError:
    print(f"Unable read/write to the file '{file_name}.txt'.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")

else:
    print(content)
    content = modified
    print(content)





