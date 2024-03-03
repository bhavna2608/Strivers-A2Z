def symmetry(n: int):
    # Write your solution here.
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print(" "*(4*(n-i)), end="")
        for j in range(i, 0, -1):
            print("*", end=" ")
        print()
    for i in range(n-1, 0, -1):
        print("* "*i, end="")
        print(" "*(4*(n-i)), end="")
        print("* "*i, end="")
        print()
    pass
