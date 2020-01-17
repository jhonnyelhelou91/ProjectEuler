n = 1000000
count = 1
number = '0'
while len(number) <= n:
    number += str(count)
    count += 1

print (int(number[1]) * int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000]))