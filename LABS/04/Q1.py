# 1. Suppose a = ["He", "th", "i", "sal"] and b = ["llo", "is", "s", "man"]
# You need to print this : ['Hello', 'this', 'is', 'salman']
# After attempting this question, make sure you may also write this query in one line.

a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]

x = zip(a, b)

for i, j in x:
    print(f"{i}{j} ", end="")