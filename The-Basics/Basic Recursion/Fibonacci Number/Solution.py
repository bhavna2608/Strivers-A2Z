from typing import List

def fib(arr, n, d):
    if d == n-1:
        return arr[:n]
    else:
        arr.append(arr[-1]+arr[-2])
        return fib(arr, n, d+1)


def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    arr = [0, 1]
    return fib(arr, n, 0)
    pass
