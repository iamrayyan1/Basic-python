# validating hexadecimal color code
# every color has a hexa code
# there is a pattern in which it is written

# the first two characters are for red, the next two for green and the last two for blue.
# characters can be 0-9 and A-F. Should begin with # and composed of 6 characters
import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[0-9A-Fa-f]{6}$"    # we are specifying 6 characters that will contain [0-9A-Fa-f] characters
    match = re.search(pattern, code)  # using ^ to show the start of the string and $ to show the end of the string
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid code")


if __name__ == "__main__":
    main()

