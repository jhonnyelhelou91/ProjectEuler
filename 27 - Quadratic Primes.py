# let y(n, a, b) = n2 + an + b
# y(0, a, b) = b => b is a prime between -1000 and 1000
# y(1, a, b) = a + b => a is odd since 2 is the only even prime
# y(n, 1000, 1000) = n2 + 1000n + 1000


def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def getPrimeCount(a, b):
    n = 0
    count = 0
    while True:
        y = n ** 2 + a * n + b
        n += 1
        if (y in primes or -y in primes):
            count += 1
        else:
            return count


n = 1000
primes = getPrimes(n)

primes = [p for p in primes if p <= n]
result = 0
result_p = 0
for a in range(-n + 1, n + 1, 2):
    for b in primes:
        key = str(a) + ' ' + str(b) + ' ' + str(a * b)
        count = getPrimeCount(a, b)
        countNegative = getPrimeCount(a, -b)
        if (count > result):
            result = count
            result_p = key
        if (countNegative > result):
            result = countNegative
            result_p = key

print(result_p, ' ', result)
