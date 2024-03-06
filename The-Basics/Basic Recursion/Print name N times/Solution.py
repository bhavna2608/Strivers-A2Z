from  typing import *

def code(lst, n):
    if n == 0:
        return lst
    else:
        lst.append("Coding Ninjas")
        return code(lst, n-1)

def printNtimes(n: int) -> List[str]:
    lst = []
    return code(lst, n)
    pass
