import sys
from os import path
from PIL import Image, ImageOps

def main():
    extension = [".jpg", ".jpeg", ".png"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        inp = sys.argv[1]
        outp = sys.argv[2]
        ext_1 = path.splitext(sys.argv[1])
        ext_2 = path.splitext(sys.argv[2])
        if ext_1[1] in extension and ext_2[1] in extension:
            if ext_1[1].lower() == ext_2[1].lower():
                shirt(inp, outp)
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")

def shirt(inp, outp):
    shirt = Image.open("shirt.png")
    with Image.open(inp) as student:
        fitted = ImageOps.fit(student, shirt.size)
        fitted.paste(shirt, mask=shirt)
        fitted.save(outp)

if __name__ == "__main__":
    main()
