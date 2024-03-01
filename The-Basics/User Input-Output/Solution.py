a = input()
b = ord(a)
if b > 64 and b < 91:
    print("1")
elif b > 96 and b < 123:
    print("0")
else:
    print("-1")
