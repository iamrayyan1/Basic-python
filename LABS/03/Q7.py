# 7. You need to read "replacement_needed.txt" file. This file has one mistake. One letter needs
# to be replaced with other letter then this sentence might have some meaning. Replace this
# letter with the desired one making logic yourself without using any library. Write your code
# in function and call that function. Handle all possible exceptions as well.

def main():
    file_name = "replacement_needed.txt"
    old = input("Enter the letter you want to change: ")
    replace = input("Enter the letter to replace it with: ")

    modified = modify(file_name, old, replace)

    print("Modified Content: ")
    print(modified)

def modify(file_name, old, replace):
    try:
        with open(file_name, "r") as file:
            content = file.read()

        print("Original Content: ")
        print(content)


        modified = ""

        for char in content:
            if char == old:
                modified += replace
            else:
                modified += char

        with open("replacement_needed.txt", "w") as file:
            file.write(modified)


    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except PermissionError:
        print("Unable to access the file.")
    except IOError:
        print("Unable to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        return modified

main()