# Ask user to enter his URL that should starts with http://www.( user url ) and then convert it into user url.com


url = input("Enter URL: ")

def process_url(url):
    if url.startswith("http://www."):
        url = url[len("http://www."):]
    elif url.startswith("https://www."):
        url = url[len("https://www."):]
    else:
        print("Enter a valid URL starting with 'http://www.' or 'https://www.'")
        exit()

    if url.endswith(".com"):
        print(url)
    else:
        print(url + ".com")

process_url(url)
