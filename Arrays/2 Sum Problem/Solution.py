def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    for i in range(n):
        if target-book[i] in book:
            return "YES"
    return "NO"
    pass
