def main():
    username = input("Input: ")
    name = shorten(username)
    print(name)

def shorten(word):
    name = ""
    for i in word:
        if not i.lower() in ["a","e","i","o","u"]:
            name += i
    return name

if __name__ == "__main__":
    main()
