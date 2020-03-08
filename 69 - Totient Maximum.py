def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

limit = 1000000
primes = getPrimes(limit)
result = 1
i = 0

while result * primes[i] < limit:
    result *= primes[i]
    i += 1

print (result)