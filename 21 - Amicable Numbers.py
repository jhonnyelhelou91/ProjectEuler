import math

numberDivisors = {
    0: 0,
    1: 0
}
def sumProperDivisors(n):
    _sqrt = (int)(math.ceil(math.sqrt(n)))
    _range = range(2, _sqrt)
    # add 1 since 1 is divisor of n and less than n
    count = 1

    for x in _range:
        if n % x == 0:
            multiplier = (int)(n / x)
            count += x + multiplier
            #print (x, multiplier)
    return count

n = 10000
for x in range(2, n):
    numberDivisors[x] = sumProperDivisors(x)

result = 0
for x in numberDivisors:
    if (numberDivisors[x] != x and numberDivisors[x] in numberDivisors and numberDivisors[numberDivisors[x]] == x):
        result += x
        #print (x, numberDivisors[x])

print (result)