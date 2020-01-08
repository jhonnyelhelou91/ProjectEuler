# https://www.mathsisfun.com/algebra/triangular-numbers.html
# nth triangular number is n(n+1) / 2
import math

def divisorsCount(n):
    _sqrt = (int)(math.ceil(math.sqrt(n)))
    _range = range(2, _sqrt)
    # add 2 since 1 and n are divisors of n
    count = 2

    for x in _range:
        if n % x == 0:
            count += 2
    return count

res = 1
n = 500
divisors = 0
while divisors <= n:
    triangular = res * (res + 1) / 2
    divisors = divisorsCount(triangular)
    res += 1

print (triangular, ' ', divisors)