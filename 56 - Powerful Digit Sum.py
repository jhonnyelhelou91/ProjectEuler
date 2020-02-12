n = 100
def getSumDigit(n):
    number = str(n)
    result = 0
    for i in range(0, len(number)):
        digit = int (number[i])
        result += digit
    return result

result = 0
for a in range(1, n):
    for b in range(1, n):
        p = a ** b
        sumDigit = getSumDigit(p)
        if result < sumDigit:
            result = sumDigit

print (result)