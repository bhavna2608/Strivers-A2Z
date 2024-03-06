from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    if m > n:
        d = dict((i,0) for i in range(1,m+1))
    else:
        d = dict((i,0) for i in range(1,n+1))
    for i in range(n):
        d[edges[i]] += 1
    arr = [d[i] for i in range(1, n+1)]
    return arr
    pass
