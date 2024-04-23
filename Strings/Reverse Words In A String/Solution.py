def reverseString(string: str) -> str:
    # Write your code from here.
    string = string.strip()
    string = list(string[::-1])
    begin = 0
    for i in range(len(string)+1):
        if i < len(string) and string[i-1] == " " and string[i] == " ":
            continue
        if i == len(string) or string[i] == " ":
            for j in range(int((i-begin)/2)):
                string[i-1-j], string[begin+j] = string[begin+j], string[i-1-j]
            begin = i+1
    return ''.join(string)
    pass
