#STRINGS

#ask user for their name with input function and assign it to a variable called name
name = input("What is your name? ")

#remove white space from the name
name = name.strip()

#capitalize the first letter of the name
name = name.capitalize()

#or title case for every word in a string
name = name.title()

#or in one line
name = input("What is your name? ").strip().title()

# print hello and the name of the user
print("hello,",  name)
#or f string
print(f"hello, {name}")
#or concatenation
print("hello, " + name)

#split the full name into first name and last name
first, last = name.split()

print("hello,", first)



