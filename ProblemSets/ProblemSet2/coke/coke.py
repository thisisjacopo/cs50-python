def main():
    buy_coke()
        

def buy_coke():
        coin = int(input("Insert a coin: "))
        total = 0
        change = 0
        left = 0
        
        #check value of coin and add to total         
        if coin == 25:
            total += 25
        elif coin == 10:
            total += 10
        elif coin == 5:
            total += 5
        elif coin == 1:
            total += 1         
        else:
            print("Error: invalid coin")
				                
			# if total is equal or more than 50 show change and return else calculate amount left and ask for another coin
        if total >= 50:
            change = total - 50
            print(f"Your Owed: {change}")
        elif total < 50:
            left = 50 - total
            print(f"Amount Due: {left}")
            buy_coke()

main()