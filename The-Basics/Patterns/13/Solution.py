def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    a = 1
    for i in range(1, n+1):
        for j in range(i):
            print(a, end=" ")
            a += 1
        print()
    pass
