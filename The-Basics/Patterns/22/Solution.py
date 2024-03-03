def getNumberPattern(n: int) -> None:
    # Write your solution here.
    for i in range((2*n)-1):
        if i == 0 or i == (2*n)-2:
            for j in range((2*n)-1):
               print(n, end="")
            print()

        elif i <= n-1:
            for j in range(i+1):
                a = n-j
                print(a, end="")
            if a > 1:
                for k in range((2*a)-3):
                    print(a, end="")
                for j in range(i, -1, -1):
                    print(n-j, end="")
            else:
                for j in range(i, 0, -1):
                    print(n-j+1, end="")
            print()

        elif i >= n:
            i = i-n
            for j in range(n-i-1):
                a = n-j
                print(a, end="")
            for k in range((2*a)-3):
                print(a, end="")
            for j in range(n-i-2, -1, -1):
                print(n-j, end="")

            print()
    
    pass
