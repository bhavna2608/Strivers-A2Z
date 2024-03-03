def alphaRamp(n: int) -> None:
    # Write your solution from here.
    for i in range(n):
        for j in range(i+1):
            print(chr(i+65), end=" ")
        print()
    pass
