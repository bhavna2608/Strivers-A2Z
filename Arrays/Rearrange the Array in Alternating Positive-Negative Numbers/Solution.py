from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    pos = []
    neg = []
    for i in range(len(a)):
        if a[i] < 0:
            neg.append(a[i])
        else:
            pos.append(a[i])
    for i in range(len(pos)):
        a[2*i] = pos[i]
        a[2*i+1] = neg[i]
    return a
    pass
