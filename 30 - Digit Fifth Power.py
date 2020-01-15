def getSumDigitPower(n):
    number = str(n)
    result = 0
    for i in range(0, len(number)):
        digit = int (number[i])
        result += powers[digit]
    
    return result

n = 5
powers = { 0: 0 }
for i in range(1, 10):
    powers[i] = i ** n

start = 2
end =  (n + 1) * powers[9]

print (start, end)
result = 0
for number in range(start, end):
    power = getSumDigitPower(number)
    if (power == number):
        #print (number)
        result += number

print (result)