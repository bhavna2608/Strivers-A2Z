from typing import List

def rec(x, arr, n):
    arr.append(x)
    if x == n:
        return arr
    else:
        return rec(x+1, arr, n)

def printNos(x: int) -> List[int]: 
    # Write your code here
    arr = []
    n = 1
    if x == 1:
        return 1
    else:
        return rec(n, arr, x)
    pass
