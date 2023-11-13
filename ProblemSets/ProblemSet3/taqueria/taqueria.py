menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
} 
prompt = "Enter your order: "
total = 0

while True: 
    try:
        item = input(prompt)
        if item.title() in menu_items:
            total += menu_items[item.title()]
            print("Total: $", end='')
            print("{:.2f}".format(total))
            
    except (EOFError, KeyboardInterrupt):
        print()
        break
            