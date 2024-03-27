from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    maxi=0
    ans=[]
    n=len(a)

    for i in range(n-1,-1,-1):
        if(a[i]>maxi):
            ans.append(a[i])
        maxi=max(maxi,a[i])

    return sorted(ans)
    pass
