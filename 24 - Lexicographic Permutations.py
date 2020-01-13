def factorial (n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
n = 1000001
count = len(digits)
result = ''

while len(result) < count:
    index = 0
    fact = factorial(count - len(result) - 1)
    while index < count and n > (index + 1) * fact:
        index += 1
    n -= index * fact
    result += digits[index]
    digits.remove(digits[index])

print (result)