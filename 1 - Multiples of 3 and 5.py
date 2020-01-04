def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return (int)(a * b / gcd(a, b))

_max = 1000
_a = 3
_b = 5
_lcm = lcm(_a, _b)
res = 0

# add multiples of a
for num in range(_a, _max, _a):
    res += num

# add multiples of b
for num in range(_b, _max, _b):
    res += num

# subtract multiples of lcm(a,b) (common for a & b)
for num in range(_lcm, _max, _lcm):
    res -= num

print(res)