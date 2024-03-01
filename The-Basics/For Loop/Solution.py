from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
a = int(input())
lst = []
lst.append(1)
lst.append(1)
if a > 2:
    for i in range(2, a): 
        lst.append(lst[i-1]+lst[i-2])
print(lst[a-1])
