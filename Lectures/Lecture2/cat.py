# Loops are used to repeat code a certain number of times or until a boolean condition is met

_ = 0

while _ <= 2:
    print("meow in while loop")
    _ += 1
    

# Lists are a collection of items that are ordered and changeable (mutable) and allow duplicate members (unlike sets)
# For loops are used to iterate through a list or other iterable object

for _ in range(3):
    print("meow in for loop")
    
#also
print("meow in simple one liner\n" * 3, end="")


#giving the user the option to choose how many times to print using while loop
#input() returns a string

while True:
    n = int(input("How many times do you want to print meow? "))   
    if n > 0:
        break
    
for _ in range(n):
    print("meow in for loop while true")
    
#with functions
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("How many times do you want to print meow? "))
        if n > 0:
            return n
        else:
            print("Please enter a positive integer.")
            
    
def meow(n):
    for _ in range(n):
        print("meow in function")
        
main()