def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    b = 1
    for i in range(n-1):
        if a[i] > a[i+1]:
            b = 0
            break
    return b
    pass
