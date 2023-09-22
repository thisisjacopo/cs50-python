#Conditions allow us to check the value of things and make decisions based on the comparison to our given condition

x = int(input('what is x? '))
y = int(input('what is y? '))

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')
    
# We can also use the 'and' and 'or' keywords to check multiple conditions at once
# 'and' will only return true if both conditions are true
# 'or' will return true if either condition is true

if x < y and x > 0:
    print('x is less than y and greater than 0')
    
if x < y or x > 0:
    print('x is less than y or greater than 0')
    