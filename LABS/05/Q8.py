# 8. You have a text document that contains dates in various formats such as 12/09/2023, 2023-09-12, and Sep 12,
# 2023. Write a Python script that uses regular expressions to extract all dates in these formats from the text.

import re

with open("doc.txt", "r") as f:
    text = f.read()


pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4})\b'

result = re.findall(pattern, text, flags=re.IGNORECASE)

print(result)
print(f"Found {len(result)} matches")

print("Dates:")
for date in result:
    print(date)