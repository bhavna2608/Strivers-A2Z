a = input() #that is how you take input in python; note that the data type of the input is always treated as a string here
b = ord(a) #The ord() function returns a number representing the unicode (ASCII) code of a specified character
if b > 64 and b < 91:
    print("1")
elif b > 96 and b < 123:
    print("0")
else:
    print("-1")
