def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

n = 1000000
primes = getPrimes(n)
phi = [i for i in range(0, n + 1)]
_sum = 0

for i in range(2, n + 1):
    if phi[i] == i:
        for j in range(i, n + 1, i):
            phi[j] = int (phi[j] / i * (i - 1))
    _sum += phi[i]

print (_sum)