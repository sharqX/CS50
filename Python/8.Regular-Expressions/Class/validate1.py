import re

email = input("What's your email? ").strip()

# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(".+@.+", email):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^\w+@\w+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
