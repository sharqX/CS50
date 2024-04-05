#while loop
i = 3
while i != 0:
    print("meow")
    i = i - 1  

a = 0
while a < 3:
    print("meow")
    a +=  1

# for loop
for i in [0, 1, 2]:
    print("meow")

for i in range(3):
    print("meow")
for _ in range(3): #without using a variable
    print("meow")

print("meow\n" * 3, end="") 

#user input loop
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

#with different functions
def main():
    number =  get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")
main()