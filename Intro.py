print("Hello from the other side")
print("I must have called a thousand times")
print("to tell you...")

import pandas as pd
s = pd.Series([1,2,3])
print(s)

from MyModule import Animal             # to import the animal class, defined in MyModule.py

zebra = Animal("Marty", 14)
zebra.description()

def sqrt(number):
    print("square root of " + str(number))
sqrt(36)


import math
print(math.sqrt(36))

from math import sqrt               # import square root from math, can quickly call this function
print(sqrt(36))

from math import *                  # import all functions from math
print(sqrt(49))
# note: might be overlap between your functions and functions from this library & existing function is then overwritten, be careful with this!

