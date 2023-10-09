
str = input("Enter tweet: ")
vowels = "aeiouAEIOU"

for char in str:
    if char in vowels:
        str = str.replace(char, "")
print(str)
