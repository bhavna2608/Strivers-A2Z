def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n-1):
        print("*"*(i+1))
    for i in range(n, 0, -1):
        print("*"*i)
    pass
