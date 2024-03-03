def nLetterTriangle(n: int):
    # Write your solution here.
    for i in range(n, -1, -1):
        for j in range(i):
            print(chr(j+65), end=" ")
        print()
    pass
