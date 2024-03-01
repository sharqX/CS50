import sys

line_count = 0

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    try:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith("#"):
                        continue
                    elif line.isspace() == True:
                        continue
                    else:
                        line_count += 1
        else:
            sys.exit("Not a Python File")
    except FileNotFoundError:
        sys.exit("File does not exist")

print(line_count)
