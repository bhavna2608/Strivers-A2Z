def symmetry(n: int):
    # Write your solution from here.
    for i in range(n, 0, -1):
        print("* "*i, end="")
        print(" "*(4*(n-i)), end="")
        print("* "*i, end="")
        print()
    for j in range(n):
        print("* "*(j+1), end="")
        print(" "*(4*(n-j-1)), end="")
        print("* "*(j+1), end="")

        print()
    pass
