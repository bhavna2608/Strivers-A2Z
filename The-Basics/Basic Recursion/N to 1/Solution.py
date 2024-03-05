from typing import List

def rec(x, arr):
    if x == 0:
        return arr
    else:
        arr.append(x)
        return rec(x-1, arr)

def printNos(x: int) -> List[int]: 
    # Write your code here
    arr = [x]
    if x == 1:
        return 1
    else:
        return rec(x-1, arr)
    pass
