def alphaHill(n: int):
    # Write your solution from here.
    for i in range(n):
        print(" "*((n-i-1)*2), end="")
        for j in range(i+1):
            print(chr(j+65), end=" ")
        for j in range(i-1, -1, -1):
            print(chr(j+65), end=" ")
        print()
    pass
