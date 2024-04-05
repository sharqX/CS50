import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    bit = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if bit:
        bits_1 = int(bit.group(1))
        bits_2 = int(bit.group(2))
        bits_3 = int(bit.group(3))
        bits_4 = int(bit.group(4))
    else:
        return False

    if bits_1 < 0 or bits_1 > 255:
        return False
    elif bits_2 < 0 or bits_2 > 255:
        return False
    elif bits_3 < 0 or bits_3 > 255:
        return False
    elif bits_4 < 0 or bits_4 > 255:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
