# Write a Python function to check if the last letter of user input string is a vowel or a consonant.



def main():
    str = input("Enter a string: ").strip().lower()

    char = str[len(str)-1]
    check(char)
    

def check(char):
    vowel = ['a', 'e', 'i', 'o', 'u']

    if char in vowel:
        print("Last letter is vowel")

    else:
        print("Last letter is consonant")


main()
