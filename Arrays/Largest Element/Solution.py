from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    # Write your code from here.

    maxi = 0
    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi

    pass
