def getSecondOrderElements(n: int,  arr: [int]) -> [int]:
    # Write your code here.
    a = max(arr)
    b = min(arr)
    arr.remove(a)
    arr.remove(b)
    return max(arr), min(arr)
    pass
