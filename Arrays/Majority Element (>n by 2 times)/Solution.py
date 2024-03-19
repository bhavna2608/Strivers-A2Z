def majorityElement(v: [int]) -> int:
    # Write your code here
    d = dict((i,0) for i in set(v))
    for i in range(len(v)):
        d[v[i]] += 1
    a = [key for key, value in d.items() if value > len(v)/2]
    return a[0]
    pass
