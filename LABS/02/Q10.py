# 10. You are creating a simple messaging tool that generates a summary message based on
# the details provided by the user. The function will build and return a message that
# incorporates all the information given.
# Write a function called build_message(**info) that takes a variable number of
# keyword arguments representing pieces of information about a person (e.g., name, age,
# city). The function should return a formatted string that includes all provided pieces
# of information.


def main():
    user_info = {
        'Name': 'Rayyan',
        'Age': 20,
        'City': 'Karachi',
        'Occupation': 'CEO'
    }

    print(build_message(**user_info))



def build_message(**info):
    message_parts = []

    for key, value in info.items():
        message_parts.append(f"{key}: {value}")

    message = "\n".join(message_parts)
    return message


main()
