from typing import Optional

def createAtoi(s: str) -> int:
    # write your code here
    s = s.strip()
    p = []
    ans = 1
    for i in range(len(s)):
        if i == 0 and s[i] == '-':
            ans = -1
        elif i == 0 and s[i] == '+':
            continue
        elif ord(s[i]) > 47 and ord(s[i]) < 58:
            p.append(s[i])
        else:
            break

    if not p:
        return 0

    result = int(''.join(p))
    result = result*ans
    
    if result > 2**31 - 1:
        return 2**31 - 1
    elif result < -2**31:
        return -2**31
    else:
        return result
    pass
