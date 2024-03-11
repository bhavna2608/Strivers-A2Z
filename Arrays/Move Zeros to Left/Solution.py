def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    count = 0
    for i in range(n):
        if a[i] == 0:
            count += 1
    for i in range(count):
        a.remove(0)
        a.append(0)
    return a
    pass
