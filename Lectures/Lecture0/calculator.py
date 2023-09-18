#INTS AND FLOATS

#integers are whole numbers, positive or negative (no decimal point)
integerNumber = 5
#floats are numbers with a decimal point
floatNumber = 5.1


x = input("what's x: ")
y = input("what's y: ")

#from input we always get a string
z =  x + y

#to convert a string to an int
x = int(x)
y = int(y)

z = x + y

#or in fewer lines by nesting the int function

x = int(input("what's x: "))
y = int(input("what's y: "))

print(x + y)

#floats
xFloated = float(input("what's x: "))
yFloated = float(input("what's y: "))
print(xFloated + yFloated)

#to round a float to the nearest integer
z = round(xFloated + yFloated)

#for long numbers we can break them with commas for readability
long = 10000000000
print(f"{long:,}")

#division
x = 10
y = 3
print(x / y) 
 
#or to round it to the nearest integer
print(f"rounded division: {round(x / y):.2f}")
