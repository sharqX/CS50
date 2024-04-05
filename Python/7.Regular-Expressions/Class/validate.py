email = input("What's your enmail? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
