# 4. Take biodata of employee from user as Name, cnic number, age, and salary save it in txt
# file. Now append this file to add contact number. Finally read this file. Handle all possible
# exceptions as well.

def main():
    file_name = input("Enter the file name: ")
    copy(file_name)

    try:
        with open(f"{file_name}.txt", 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"The file '{file_name}.txt' was not found.")
    except IOError:
        print("Unable to read/write from the file.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    else:
        print(f"\n{content}")


def copy(file_name):
    name = input("Enter name: ")
    cnic = input("Enter CNIC number: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    try:
        with open(f"{file_name}.txt", 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except IOError:
        print("Unable to read/write to the file.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


    else:
        try:
            contact = input("Enter contact number: ")

            with open(f"{file_name}.txt", 'a') as file:
                file.write(f"Contact Number: {contact}\n")

        except FileNotFoundError:
            print(f"The file '{file_name}.txt' was not found.")
        except IOError:
            print("Unable to read/write to the file.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")


main()



