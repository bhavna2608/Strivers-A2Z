def countDigits(n: int) -> int:
    a = str(n)
    count = 0
    for i in range(len(a)):
        if a[i] != '0':
            if n%int(a[i]) == 0:
                count += 1
    return count
    pass
