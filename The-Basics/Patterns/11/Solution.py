def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    start = 0
    for i in range(n):
        if i%2 == 0:
            start = 1
        else:
            start = 0
        if start == 1:
            for j in range(i+1):
                if j%2 == 0:
                    print("1 ", end="")
                else:
                    print("0 ", end="")
        
        else:
            for j in range(i+1):
                if j%2 == 0:
                    print("0 ", end="")
                else:
                    print("1 ", end="")
        print()
    
    pass
