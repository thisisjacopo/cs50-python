greet = input("Hello, how you doing? ")

greet_list = greet.lower().strip().replace(',', "").split()

if greet_list[0] == "hello":
    print("$0")
elif greet_list[0][0] == 'h':
    print("$20")
else:
    print("$100")