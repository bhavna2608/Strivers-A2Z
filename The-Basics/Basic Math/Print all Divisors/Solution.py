## giving TLE for one test case. 

from math import * 

def div(n):
    sums = 1+n
    if n > 2:
        for i in range(2, int(n/2)+1):
            if n%i == 0:
                sums += i
    return sums

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    sums = 1
    for i in range(2, n+1):
        sums += div(i)
    return sums
    pass
