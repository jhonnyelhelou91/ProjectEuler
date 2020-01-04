#lcm (2, 3) = 6
#lcm (6, 4) = 12
#lcm (12, 5) = 60
#lcm (60, 7) = 420
#lcm (420, 8) = 840
#lcm (840, 9) = 2520
#lcm (2520, 10) = 2520

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return (int)(a * b / gcd(a, b))

_range = range(1, 20)
res = 1
for x in _range:
    print('lcm(', res, ',', x, ')')
    res = lcm(res, x)

print (res)