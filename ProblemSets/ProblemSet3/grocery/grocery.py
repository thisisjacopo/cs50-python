total = 0
items = {}
prompt = "Enter your order: "
while True:
    try:
        item = input(prompt)
        if item.title() in items:
            items[item.title()] += 1
        else:
            items[item.title()] = 1
    except (EOFError, KeyboardInterrupt):
        print()
        break

for item in sorted(items):
    print(items[item], item.upper())

