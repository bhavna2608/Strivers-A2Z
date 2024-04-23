def maxDepth(s:str) -> int:
    # Write your code here.
    length = 0
    depth = 0
    max_l = 0
    for i in range(len(s)):
        if s[i] == "(":
            length += 1
            if length > max_l:
                max_l = length
        elif s[i] == ")":
            length -= 1
    return max_l
    pass
