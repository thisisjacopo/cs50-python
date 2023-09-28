expression = input("Enter an arithmetic expression: ")

values = []
operators = []
for i in expression:
    if i.isdigit():
        values.append(i)
    else:
        operators.append(i)

result = int(values[0]) + operators[0] + int(values[1])

print(float(result))