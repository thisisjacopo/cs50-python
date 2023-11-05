# exceptions are used to handle errors in python
# try and except are used to handle errors
# try block lets you test a block of code for errors
# except block lets you handle the error
# pass is used to handle the error without crashing the program
#raise is used to raise an exception when a certain condition is met 

def main():
    x = get_int("Enter a number: ")
    print(f"x is {x}")

def get_int(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("Invalid input, x is not an integer")
            pass
    
main()