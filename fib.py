#fib.py

import time
from functools import lru_cache
import matplotlib.pyplot as plt

times = []
#Implemented a timer decorator along with the future y-axis time value
def timer(function):
    def startfinish(n):
        start = time.time()    #set start time
        result = function(n)   #run function
        end = time.time()      #set end time
        finished = end - start
        times.append(finished)
        print(f"Finished in {finished: .8f}s: f({n}) -> {result}") #print results
        return(result)
    return(startfinish)

@lru_cache
@timer 
def fib(n:int) -> int:
    if n < 2:
        return(n)
    return(fib(n-1) + fib(n-2))

if __name__ == "__main__":
    fib(100)
    nvals = list(range(101))

plt.plot(nvals, times)
plt.xlabel("'n' in Fib Number Calculation")
plt.ylabel("Time to Calculate(seconds)")
plt.xlim(0, 100)
plt.ylim(0, 0.009)
plt.show()
