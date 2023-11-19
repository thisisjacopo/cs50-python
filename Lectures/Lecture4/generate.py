#libraries are pre-written code that you can use in your own code to perform certain actions without having to write your own code
#random is a library that allows you to generate random numbers
#choice is a function that allows you to choose a random element from a list

import random

coin = random.choice(['heads', 'tails'])
print(coin)

#from imports a specific function from a library so that you don't have to type the library name every time you want to use the function
from random import choice

number = choice([1, 2, 3, 4, 5])
print(number)

#randint is a function that allows you to generate a random integer between two numbers
from random import randint

random_number = randint(1, 100)
print(random_number)

#shuffle is a function that allows you to shuffle a list
from random import shuffle

cards = ['Jack', 'Queen', 'King', 'Ace']
shuffle(cards)
for card in cards:
    print(card)
    
