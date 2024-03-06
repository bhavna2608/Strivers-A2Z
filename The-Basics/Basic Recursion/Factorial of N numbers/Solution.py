from typing import *

def fact(arr, z, n):
    if arr[-1]*z <= n:
        arr.append(arr[-1]*z)
        return fact(arr, z+1, n)
    else:
        return arr

def factorialNumbers(n: int) -> List[int]:
    # Write your code here.
    arr = [1]
    return fact(arr, 2, n)
    pass
