import numpy as np
from multiprocessing import Pool
import time

# This program uses a basic way to parallelize computation.
# Here we are using the multiprocessing module.
# We are creating a 'pool' of processes that can execute a function in parallel.
# Specifically we are using the 'map' function that applies the same function to a list of data.

def doubleplusone(x):
    return x*x+1

#biglist = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
biglist = np.arange(0,10000)

# Initialize to None
newlist = None

# This checks to see if this is the 'main' process or a sub-process
# This is common in parallel Python programs
if __name__ == '__main__':

    # Record the start and end times
    pstart = time.time()
    
    # Launch a pool of 2 processes for parallelism, map the big list to the function
    with Pool(2) as p:
        newlist = p.map(doubleplusone, biglist)
    pend = time.time()

    # Do the same thing, but using traditional Python functions
    sstart = time.time()
    slist = list(map(doubleplusone, biglist))
    send = time.time()


print("List sums")
print(np.sum(newlist))
print(np.sum(slist))

print("Times")
print("Parallel time (seconds)", pend-pstart)
print("Serial time (seconds)", send-sstart)
