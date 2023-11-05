# exceptions are used to handle errors in python
# try and except are used to handle errors
# try block lets you test a block of code for errors
# except block lets you handle the error
# finally block lets you execute code, regardless of the result of the try and except blocks
# raise keyword is used to raise an exception
# assert keyword is used to assert if something is true

try:
    x = input("Enter a number: ")
    print(f"Your number is {x}")
except ValueError:
    print("Invalid input, x is not an integer")