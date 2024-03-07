def shift(i, j, arr):
    t = arr[i]
    arr[i] = arr[j]
    if j == i+1:
        arr[j] = t
        return arr
    elif j>i+1:
        for k in range(j, i+1, -1):
            arr[k] = arr[k-1]
        arr[i+1] = t
        return arr

def compare(i, j, arr):
    if i == -1:
        shift(0, j, arr)
        return arr
    if arr[j] < arr[i-1]:
        return compare(i-1, j, arr)
    else:
        shift(i, j, arr)
        return arr


def insertionSort(arr):
    # write your code here !!!
    n = len(arr)
    for i in range(1, n):
        compare(i, i, arr)
