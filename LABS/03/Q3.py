
# 3. Write a python program that takes any two lists from user having same number of
# elements. Make a dictionary from these two lists in such a way that first element of first list
# will be key and first element of second list will be its associated value and so on. Store the
# dictionary in a text file. Handle all possible exceptions as well.
# Note: do not use any library. Make logic yourself.

file_name = input("Enter the file name: ")
lst1 = input("Enter elements of the first list: ").split()
lst2 = input("Enter elements of the second list: ").split()

try:
    if len(lst1) != len(lst2):
        raise ValueError("Both lists must have the same number of elements.")

    dictionary = {}
    for i in range(len(lst1)):
        dictionary[lst1[i]] = lst2[i]


except Exception as e:
    print(f"Unexpected error occurred: {e}")

else:
    try:
        with open(f"{file_name}.txt", 'w') as file:
            for key, value in dictionary.items():
                file.write(f"{key}: {value}\n")

        with open(f"{file_name}.txt", 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"The file '{file_name}.txt' could not be found or created.")
    except IOError:
        print(f"Unable to read/write to the file '{file_name}.txt'.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    else:
        print(content)

