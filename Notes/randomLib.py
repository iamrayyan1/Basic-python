import random

cards = ["jack", "queen", "king", "ace"]


def main():
    random.seed(0)    # setting the seed, gives us random choices but those choices remain consistent.
    print(random.choices(cards))        # choose one card
    print(random.choices(cards, k=2))   # chooses k num of cards
    print(random.sample(cards, k=2))    # this will give second result without replacement(means we will always get two distinct cards)
    print(random.choices(cards, weights=[100,0,0,0], k=2))   # setting weights to how often we will get a certain card. In this case we set jack probability to 100.


main()



# style  - PEP 8(style guide)
# Indentation
# Tabs or Spaces
# Maximum Line Length
# Blank lines
# Imports
# ...

# pylint - a tool to style.
# pycodestyle - a program that you can run on program and will style your program
# black - another tool.   just write "black yourFileName" and your code will be formatted.

# reformat using Ctrl+Alt+L