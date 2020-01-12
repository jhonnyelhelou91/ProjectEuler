import math

abundantNumbers = {}
def sumProperDivisors(n):
    if (n == 1):
        return 1
    _sqrt = (int)(math.ceil(math.sqrt(n)))
    _range = range(2, _sqrt)
    # add 1 since 1 is divisor of n and less than n
    _sum = 1

    for x in _range:
        if n % x == 0:
            multiplier = (int)(n / x)
            _sum += x + multiplier
            #print (x, multiplier)
    if (_sqrt ** 2 == n):
        _sum += _sqrt
    return _sum

def isSumAbundant(n):
    for x in abundantNumbers:
        diff = n - x
        if (diff > 0 and diff in abundantNumbers):
            return True
    return False

n = 28123
_range = range(1, n + 1)
for x in _range:
    _sum = sumProperDivisors(x)
    if (_sum > x):
        abundantNumbers[x] = True

result = 0
for x in _range:
    if (not isSumAbundant(x)):
        result += x

print (result)