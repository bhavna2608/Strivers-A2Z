def romanToInt(s:str) -> int:
    # Write your code here
    dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

    sums = 0
    for i in range(len(s)-1):
        if dic[s[i]] >= dic[s[i+1]]:
            sums += dic[s[i]]
        else:
            sums -= dic[s[i]]
    sums += dic[s[len(s)-1]]

    return sums
    pass
