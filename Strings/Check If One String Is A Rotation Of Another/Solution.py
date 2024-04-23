def isCyclicRotation(p: str, s: str) -> int:
    # Write your code here.
    if len(s) != len(p):
        return 0

    else:
        if s == p:
            return 1
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == p:
                return 1

    return 0
    pass
