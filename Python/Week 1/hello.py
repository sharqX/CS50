#The "Hello, World" Program
print("Hello, World")

#inputs, variables and return values
name = input("What is your name? ")
print("Hello,",name)

#parameters
print("hello,",name,sep=" ") 
print("hello, ", end="")  
print(name)

#printing qoutes
print("Hello,'friend'")
print("Hello, \"friend\" ")
 
#str

# formating string
print(f"Hello, {name}")

#remove whitespace from  str
name = name.strip()

#Capitalize user's name
name = name.capitalize()

#title
name = name.title()

#chaining functions
name = name.strip().title()

#int
x = input("What's x ")
y = input("What's y ")

print("Addition of the numbers is ",int(x) + int(y))

#float
x = input("What's x ")
y = input("What's y ")

print("Addition of the numbers is ",float(x) + float(y))

#round function
x = float(input("What's x "))
y = float(input("What's y "))

z = round(x+y)

print(z)

#format a number
print(f"{z:,}")

#nearest number of integer
z = round(x/y,2)

print(f"{z:.2f}")

#USER DEFINED FUNCTIONS
def hello(to="world"):
    print("hello,", to)

hello()
name =  input("What's your name? ")
hello(name)

#Convention of defining functions
def main():
    name =  input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

#scope: Scope refers to a variable only existing in the context in which you defined it.

#return
def main():
    x = int(input("What's X?"))
    print("x squared is", square(x))

def square(n):
    return n * n
    #return n ** 2
    #return pow(n,2)

main()

name = name.lower