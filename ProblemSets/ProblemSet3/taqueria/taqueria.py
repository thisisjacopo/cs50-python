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
def main(): 
    try:
        item = input(prompt)  
        get_total(item.title())
    except (EOFError, KeyboardInterrupt):
        print(f"Total: ${total}")

def get_total(item:str):
    try:
        total += menu_items[item]
        main()
        print(f"Total: ${total}")
    except (EOFError, KeyboardInterrupt):
        print(f"Total: ${total}")
    except (ValueError, ZeroDivisionError, TypeError, KeyError, AttributeError, IndexError, NameError):
        main()
        
    
main()