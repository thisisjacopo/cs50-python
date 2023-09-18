#FUNCTIONS
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Functions need to be defined before they are called.


#defining a function

def main():
    name = input("What is your full name? ").strip().title()
    hello(name)

def hello(to="World"):
    print("hello,", to)

#will print the default value of the parameter
hello()


#calculating function

def main_calc():
    x = int(input("what's x: "))
    print("x squared is:", square(x))
    
def square(x):
    return x * x

main()
main_calc()