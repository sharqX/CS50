def main():
    mass = input()
    energy = convert(mass)
    print(energy)

def convert(mass):
    mass1 = int(mass) * (300000000 **2)
    return mass1

main()
