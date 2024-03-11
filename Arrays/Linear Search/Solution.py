def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    if num in arr:
        for i in range(n):
            if arr[i] == num:
                return i
    else:
        return -1
    pass
