expression = input("Enter an arithmetic expression: ")

expression = expression.split(' ')

operator = expression[1]

if operator == '+':
    result = int(expression[0]) + int(expression[2])
elif operator == '-':
    result = int(expression[0]) - int(expression[2])
elif operator == '*':
    result = int(expression[0]) * int(expression[2])
elif operator == '/':
    result = int(expression[0]) / int(expression[2])
else:
    result = int(expression[0]) % int(expression[2])
    
print(float(result))