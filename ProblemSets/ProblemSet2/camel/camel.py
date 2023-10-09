def main():
    camel = input("Insert name in camel case: ")
    print(to_camel_case(camel))
    
def to_camel_case(string):
    for letter in string:
        if letter.isupper():
            string = string.replace(letter, f"_{letter.lower()}")
    return string

main()
