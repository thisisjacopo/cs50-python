#ask user for their name with input function and assign it to a variable called name
name = input("What is your name? ")

#remove white space from the name
name = name.strip()

#capitalize the first letter of the name
name = name.capitalize()

# print hello and the name of the user
print("hello,",  name)
#or f string
print(f"hello, {name}")
#or concatenation
print("hello, " + name)

