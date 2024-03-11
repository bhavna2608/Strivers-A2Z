from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    d = {element: 0 for element in set(arr)}
    for i in range(len(arr)):
        d[arr[i]] += 1
    a = [key for key, value in d.items() if value == 1]
    return a[0]
    pass
