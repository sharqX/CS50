from validator_collection import validators, errors


def main():
    print(email(input("What's your eamil? ")))


def email(e):
    try:
        if validators.email(e, allow_empty=True):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
