# Write a program that accepts a word from the user and reversesit using loop. For example,‘Pakistan’ becomes‘natsikaP’.

word = input("Enter string: ")
new_word = ""

# range(start, stop, step) -> python documentation
for i in range(len(word)-1, -1, -1):
    new_word += word[i]

print(new_word)


# or

word = input("Enter string: ")
new_word = ""

for i in word:
    new_word = i + new_word 

print(new_word)
