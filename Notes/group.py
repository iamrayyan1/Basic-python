import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    # we can name the capture group using (?P<name>...)
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Enter a number: ")

    match = re.search(pattern, number)
    if match:
        print("Valid")
    else:
        print("Invalid")

    # extracting country calling code using grouping/parentheses
    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")     # inside match.group() we can use the name of the capture group we gave above
        print(country_code)
        print(locations[country_code])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()


# more program on pattern.py