from os import *
from sys import *
from collections import *
from math import *

n = int(input())
b = str(n)
a = len(b)
sum = 0
for i in range(a):
	sum += int(b[i])**(a)
if sum == n:
    print("true")
else:
    print("false")
