#We can loop through a list of items and check if they match a condition, and we can also use the reminder (%) operator 
#to check if a number is even or odd

x = int(input('what is x? '))

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
    
#We can also use the 'in' keyword to check if a value is in a list

my_list = [1, 2, 3, 4, 5]

if x in my_list:
    print('x is in my_list')
else:
    print('x is not in my_list')
    
#We can also use the 'not' keyword to check if a value is not in a list

if x not in my_list:
    print('x is not in my_list')
else:
    print('x is in my_list')
    
    
#We can also use the 'not' keyword to check if a value is not in a list

if x not in my_list:
    print('x is not in my_list')
else:
    print('x is in my_list')

#We can also use the 'is' keyword to check if two values are the same object

y = x

if x is y:
    print('x is y')
else:
    print('x is not y')
    
#We can also use the 'is not' keyword to check if two values are not the same object

if x is not y:
    print('x is not y')
else:
    print('x is y')
    