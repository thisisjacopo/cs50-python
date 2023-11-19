#accessing words that we input in the command line with sys module
#sys module is a module that allows us to access the command line arguments
#sys.argv is a list that contains the command line arguments

import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments.")

for arg in sys.argv[1:]:
    print(f'Hello, my name is {arg}')
