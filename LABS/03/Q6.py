# Create a function that asks the user to enter a sentence then writes the sentence to a text file
# named "questions.txt" if it's a question. Handle all possible exceptions as well.


sentence = input("Please enter a sentence: ")
file_name = "questions.txt"

if sentence.endswith('?'):
    try:
        with open(file_name, "a") as file:
            file.write(sentence + "\n")

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Unable to read/write to the file.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    else:
        with open(file_name, "r") as file:
            content = file.read()
        print(content)

else:
    print("Not a question.")


