# 7. You have a block of text that contains several email addresses scattered throughout. Write a Python
# script that uses regular expressions to extract all valid email addresses from the text.

import re

text = " "   # text containing email addresses
pattern = r"^\w+@\w+\.(edu|com|gov|org|net)$"

result = re.findall(pattern, text, flags=re.IGNORECASE)

print(result)
print(f"Found {len(result)} matches")

print("Email addresses:")
for email in result:
    print(email)

