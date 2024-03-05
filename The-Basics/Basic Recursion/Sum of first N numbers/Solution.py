## via recursion
from typing import List

def sums(n, sum1):
    if n == 1:
        return sum1
    else:
        sum1 += n
        return sums(n-1, sum1)

def sumFirstN(n: int) -> int:
    Write your code here.
    sum1 = 1
    return sums(n, sum1)
    pass

## via direct formula
# def sumFirstN(n: int) -> int:
#     # Write your code here.
#     return int((n*(n+1))/2)
#     pass
