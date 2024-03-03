def reverseBits(n):
    # Write your code here.
    b = '{:032b}'.format(n)
    b = str(b)
    a = int(b[::-1], 2)
    return a
    pass
