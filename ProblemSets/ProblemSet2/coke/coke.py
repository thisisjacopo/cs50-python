def main():
    buy_coke()
        

def buy_coke():
    total = 0
    coke = 50
    change = total
    left = coke

    while total < 50:
        coin = int(input("Insert a coin: "))
        if coin in { 5, 10, 25, 1}:
            total += coin
            left = coke - total
            change = total - coke
            print(f"Amount Due: {left}")
        else:
            print(f"Amount Due: {left}")
        
    print(f"Change Owed: {change}")

main()