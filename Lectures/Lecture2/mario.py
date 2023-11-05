def main():
    print_columns(3)
    print_rows(4)
    print_square(5)
    print_square_smart(3)
    
def print_columns(height):
    print("#\n" * height, end="")
    
def print_rows(width):
    print("?" * width)
        
def print_square(size):
    #for each row in square
    for _ in range(size):
        #for each @ in row
        for _ in range(size):
            #print @
            print("[@]", end="")    
        #print new line
        print()
        
def print_square_smart(size):
    for _ in range(size):
        print("[#]" * size)
         
main()