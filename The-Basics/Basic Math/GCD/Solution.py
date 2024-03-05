def calcGDC(n:int, m: int) -> int:
    if n > m:
        t = m
        m = n
        n = t

    if n == m or m%n == 0:
        return n
    
    else:
        return calcGDC(n, m%n)
        
    pass
