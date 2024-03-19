from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
	# Write your code here
	mid = 0
	low = 0
	high = n-1
	while(mid <= high):
		if arr[mid] == 0:
			arr[mid], arr[low] = arr[low], arr[mid]
			low += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			arr[high], arr[mid] = arr[mid], arr[high]
			high -= 1
	pass
