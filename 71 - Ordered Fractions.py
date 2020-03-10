def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
n = 1000000
_max = 3 / 7
result = [0, 1, 0]

for den in range(2, n + 1):
    #skip numbers and start with the closest numerator
    num = max([int(_max * den), 1])
    while num / den < _max:
        if gcd(num, den) == 1:
            res = num / den
            if res < _max and num > result[-1]:
                result = [num, den, res]
        num += 1
    
print (result)