import re

# email = input("What's your email? ").strip().lower()

# if re.search(r"^\w+@\w+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")

email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.com$", email,  re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")


if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email,  re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
