from typing import List

def swap(j, c, arr):
    t = arr[j]
    arr[j] = arr[c]
    arr[c] = t
    return arr

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(n):
        flag = 0
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                swap(j+1, j, arr)
                flag = 1
        if flag == 0:
            break
    pass
