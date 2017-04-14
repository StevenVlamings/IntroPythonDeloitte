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

from joblib import Parallel, delayed
import multiprocessing
import time

def myfunction(i):          # takes a number, prints it, wait 2 seconds & then return the number (simulating a heavy process / calculation)
    print(i)
    time.sleep(2)
    return(i)

if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        myresults = myfunction(i)
    print("SERIAL", time.time()-start)
    num_cores = multiprocessing.cpu_count()
    print("Number of cores used: " + str(num_cores))
    start=time.time()
    results = Parallel(n_jobs = num_cores)(delayed(myfunction)(i) for i in range(10))
    print("PARALLEL", time.time()-start)
    print(results)
