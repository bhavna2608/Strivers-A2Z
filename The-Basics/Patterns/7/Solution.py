def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        print(" "*(n-i-1), end="")
        print("*"*((2*i)+1))
    pass
