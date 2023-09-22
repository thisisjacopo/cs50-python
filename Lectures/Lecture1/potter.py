caracther = input("Enter a character: ")

if caracther == "harry":
    print("Gryffindor")
elif caracther == "hermione":
    print("Gryffindor")
elif caracther == "draco":
    print("Slytherin")
else:
    print("who?")
    
# This can be shorten like:

if caracther == "harry"  or caracther == "hermione":
    print("Gryffindor")
elif caracther == "draco":
    print("Slytherin")
else:
    print("who?")
    
    
# This can be shorten like:

if caracther in ["harry", "hermione"]:
    print("Gryffindor")
elif caracther == "draco":
    print("Slytherin")
else:
    print("who?")
    
# or by using match:    

match caracther:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?")
        
# this can be improved by using the | operator:

match caracther:
    case "harry" | "hermione":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?")
        