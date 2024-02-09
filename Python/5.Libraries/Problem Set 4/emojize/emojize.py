import emoji

x = input("Input: ").strip()
a = emoji.emojize(x,language="alias")

print(a)
