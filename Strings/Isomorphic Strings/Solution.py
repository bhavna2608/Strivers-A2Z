def areIsomorphic(str1: str, str2: str) -> bool:
    # Write your code here
    d1 = {}
    d2 = {}
    if len(str1) != len(str2):
        return False
    
    else:
        for i in range(len(str1)):
            if str1[i] not in d1 and str2[i] not in d2:
                d1[str1[i]] = str2[i]
                d2[str2[i]] = str1[i]
            else:
                if str2[i] not in d2 or str1[i] != d2[str2[i]]:
                    return False
                if  str1[i] not in d1 or str2[i] != d1[str1[i]]:
                    return False
    
    return True

    pass
