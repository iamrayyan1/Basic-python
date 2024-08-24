# goal is to prompt user for the url of their Twitter profile and extract from it the user's username

url = input("URL: ").strip()
print(url)

# ignore everything before username if url and extract username only. for eg: https://twitter.com/davidjmalan  : ignore https://twitter.com/ and extract: davidjmalan

# replace() method can be used to extract the username. We will store only username part and replace rest with an empty string "".
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# but still it's very fragile, where in some cases it won't work. since there is lot user could type so there is alot of cases to handle.

# another method could be using url.removeprefix
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

# regex can be use to create patterns and group things

import re
url = input("URL: ").strip()

# another function in re library is "re.sub()" substitute
# re.sub(pattern, repl, string, count=0, flags=0)   # repl means replacement string

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")

# solving protocol, sub domain,
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)   # adding ^ at the start and adding \ before . so we litreally mean a .
print(f"Username: {username}")    # using ? before s to allow both http and https. # and then grouping (www.) and making it optional to write.
                                  # also making the (https://) optional since people often directly start with www. or directly write website name.


# there is a possibility that user might right some other url, that's not even of twitter
# so we can use re.search to solve the problem instead of re.sub

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)   # using parentheses to capture the username
if matches:
    print(f"Username:", matches.group(3))  # using 3 since we are storing username in the 3rd parentheses

# matches print None if the string is empty

# using Walrus Operator
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(3))

# solving it using non capturing version: (?:...) means we are making groups/parentheses, but we don't wanna capture it inside matches
matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))   # so now we can using 1 since only one of the parentheses are capturing, rest are non-capturing (?:...)

# restricting on what username can be: [a-z0-9_]
matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))

# re.split can be used to split using split multiple characters
# re.split(pattern, string, maxsplit=0, flags=0)

# re.findall allows you to search for multiple copies of the same pattern in different places in the string so you can manipulate more than just one
# re.findall(pattern, string, flags=0)

# check groups.py for adv concepts
