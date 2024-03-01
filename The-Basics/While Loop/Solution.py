a = input()
i = even_sum = odd_sum = 0
while(i < len(a)):
    if int(a[i]) % 2 == 0:
        even_sum += int(a[i])
    else:
        odd_sum += int(a[i])
    i += 1
print(even_sum," ", odd_sum)
