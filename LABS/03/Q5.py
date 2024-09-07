# 5. Take input from user below dictionary having name and age pair. Save this dictionary in
# json file. Now load this json file and Print name of person having maximum age and also
# print if anyone has the same age by making logic yourself without using any library:
# dictionary = {'Ali': 23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23'}
# Handle all possible exceptions as well.

import json


def main():
    people = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
    file_name = input("Enter the file name: ")

    data = func(file_name, people)

    try:
        maximum = max(data.values())
        name = ""
        for key, value in data.items():
            if value == maximum:
                name += key

    except NameError:
        print("Data not found")
    except ValueError:
        print("Failed to decode the data")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    else:
        print(f"Person with max height: {name} of height {maximum}")


def func(file_name, data):
    try:
        with open(f"{file_name}.txt", 'w') as file:
            json.dump(data, file)

    except FileNotFoundError:
        print(f"The file '{file_name}.txt' was not found")
    except IOError:
        print("Unable to read/write to the file")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    else:

        try:
            with open(f"{file_name}.txt", 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            print(f"The file '{file_name}.txt' was not found.")
        except IOError:
            print("Unable t0 read/write from the file.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

        else:
            return data




main()

