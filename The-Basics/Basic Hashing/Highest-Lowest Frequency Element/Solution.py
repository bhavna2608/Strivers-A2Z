from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    a = set(v)
    d = dict((i,0) for i in a)
    for i in range(len(v)):
        d[v[i]] += 1
    mins = min(d.values())
    maxs = max(d.values())
    min_a = min([key for key, value in d.items() if value == mins])
    max_a = min([key for key, value in d.items() if value == maxs])

    return max_a, min_a
    pass
