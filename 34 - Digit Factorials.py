# n < 10^d
# d * 9! < 10^d
# log(d) * log(9!) < d log(10)
# log(d) * 5.56 < d log(10)
# log(d) * 5.56 < d
# d - log(d) > 5.56
import math

def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n - 1)

def sumFactorials(n):
    number = str(n)
    result = 0
    for digit in number:
        result += digitFactorials[int(digit)]
    return result
digitFactorials = {}
for digit in range(0, 10):
    digitFactorials[digit] = factorial(digit)

n = 3
fact = factorial(3)
result = 0

while len(str(n)) - math.log(len(str(n))) < 5.56:
    fact = sumFactorials(n)
    if (fact == n):
        result += fact
        print(n, fact)
    n += 1

print (result)