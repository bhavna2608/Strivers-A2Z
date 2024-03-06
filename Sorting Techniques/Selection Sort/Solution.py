from typing import List

def swap(j, c, arr):
    t = arr[j]
    arr[j] = arr[c]
    arr[c] = t
    return arr

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n = len(arr)
    count = -1
    for i in range(n):
        t = min(arr[i:])
        for j in range(i, n):
            if arr[j] == t:
                count += 1
                swap(j, count, arr)
                break
    return arr
    pass
