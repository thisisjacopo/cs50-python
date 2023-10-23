def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #create an array of each character in the string
    chars = list(s)
    
    #check that it's min 2 and max 6 characters long
    if len(chars) < 2 or len(chars) > 6:
        return False
    
    #check if the first 2 characters are letters
    if not chars[0].isalpha() or not chars[1].isalpha():
        return False
    
    
    #check if there is a number in the last 4 characters, if so, the first one cannot be 0 and the last character cannot be a letter
    if chars[2].isdigit() or chars[3].isdigit() or chars[4].isdigit() or chars[5].isdigit():
        if chars[2] == "0":
            return False
        if chars[-1].isalpha():
            return False
        
        
    for i in range(2, len(chars)):
        if chars[i].isdigit() and chars[i] != chars[-1]:
            if chars[i+1].isalpha():
                return False
    
    #check that there are no special characters, only letters and numbers
    for char in chars:
        if not char.isalpha() and not char.isdigit():
            return False
    
    
    return True
        
        

main()