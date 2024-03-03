def alphaTriangle(n: int):
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(chr(n+64-j), end=" ")
        print()
    pass
