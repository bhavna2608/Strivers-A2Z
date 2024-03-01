from typing import *
from math import pi

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    match ch:
        case 1:
            return round(pi*a[0]*a[0], 5)
        case 2:
            return format(a[0]*a[1], '.5f')
    pass
