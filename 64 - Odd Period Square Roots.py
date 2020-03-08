def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def getPeriod(n):
    sqrt = int(n ** 0.5)
    period = 0
    a = sqrt
    num = 0
    den = 1
    if sqrt ** 2 == n:
        return period

    while a != 2 * sqrt or period == 0:
        num = den * a - num
        den = int((n - num * num) / den)
        a = int((sqrt + num) / den)
        period += 1
    
    return period

n = 10000
result = 0

for num in range(1, n + 1):
    period = getPeriod(num)
    if period % 2 == 1:
        result += 1

print (result)