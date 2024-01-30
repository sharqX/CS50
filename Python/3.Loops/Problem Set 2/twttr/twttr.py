def main():
    inpt = input("Input: ")
    remove_vowel(inpt)

def remove_vowel(n):
    vowel = ["a", "e" ,"i" ,"o" ,"u"]
    for i in n:
        if not i.lower() in vowel :
            print(i, end="")
main()
