def b(n, string, e, tf):
    if n <= e and tf == 0:
        return False
    elif n <= e and tf == 1:
        return True
    else:
        if string[n] == string[e]:
            tf = 1
            return b(n-1, string, e+1, tf)
        else:
            tf = 0 
            return False

def isPalindrome(string: str) -> bool:
    n = len(string)
    return b(n-1, string, 0, 0)
    pass
