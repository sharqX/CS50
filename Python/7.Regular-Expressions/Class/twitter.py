import re
url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/?", "", url)
# print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):

# if matches:
    print("Username: ", matches.group(1))
    # print("Username: ", matches.group(2))