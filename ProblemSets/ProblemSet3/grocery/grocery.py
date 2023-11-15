total = 0
items = {}
prompt = ""
while True:
    try:
        item = input(prompt)
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except (EOFError, KeyboardInterrupt):
        for item in sorted(items):
            print(items[item], item.upper(), end='\n')
        break