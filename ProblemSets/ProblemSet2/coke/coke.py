def main():
    buy_coke()
        

def buy_coke():
        coin = int(input("Insert a coin: "))
        total = 0
        change = 0
        left = 0
        coke = 50
        
        #while the value of the coin is different from 50, ask the user to insert the remaining coins
        while coin != 50:
            
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
                
            if total > coke:
                change = total - coke
                print(f"Your Owed: {change}")
                return
            #if the total value of the coins inserted is less than 50, calculate the left amount
            elif total < coke:
                left = coke - total
                print(f"Amount Due: {left}")
            coin = int(input("Insert a coin: "))
            
        if total == coke:
            print(f"Changed Owed: {change}")
        else:
            buy_coke()



main()