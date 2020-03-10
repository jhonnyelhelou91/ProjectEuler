def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
n = 12000
_min = 1 / 3
_max = 1 / 2
result = 0

for den in range(2, n + 1):
    #skip numbers and start with the closest numerator
    num = min([
        int(_min * den),
        int(_max * den)
    ])
    while num / den <= _max:
        if gcd(num, den) == 1:
            res = num / den
            if _min < res < _max:
                result += 1
        num += 1
    
print (result)