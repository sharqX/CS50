def main():
    yell("This is CS50")
    # yell(["This" ,"is","CS50"])

# def yell(phrase):
    # print(phrase.upper())

# def yell(*words): 
#     uppercased = []
#     for word in words:
#          uppercased.append(word.upper())
#     print(*uppercased)

# def yell(*words):
#       uppercased = map(str.upper, words) #map function
#       print(*uppercased)

def yell(*words):
      uppercased = [word.upper() for word in words] #list comprehension
      print(*uppercased)

if __name__=="__main__":
    main()