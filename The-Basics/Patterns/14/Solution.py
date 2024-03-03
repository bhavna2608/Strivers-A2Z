def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(chr(j+65), end=" ")
        print()
    pass
