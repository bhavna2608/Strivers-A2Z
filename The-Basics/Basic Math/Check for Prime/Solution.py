from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
prime = 0
if n >= 11:
    if n%2 == 0 or n%5 == 0 or n%3 == 0 or n%7 == 0:
        print("NO")
    else:
        for i in range(11, int(sqrt(n))):
            if i%2 == 0 or i%5 == 0 or i%3 == 0 or i%7 == 0:
                continue
            else:
                if n%i == 0:
                    prime = 1
                    print("NO")
                    break
                else:
                    prime = 0

        if prime == 0:
            print("YES")
    
else:
    if n == 2 or n == 3 or n == 5 or n == 7:
        print("YES")
    else:
        print("NO")

