def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n = len(arr)
    a = arr[:k]
    for i in range(n-k):
        arr[i] = arr[i+k]
    for i in range(n-k, n):
        arr[i] = a[i-n+k]
    return arr
    pass
