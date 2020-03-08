import sys

def isPermutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def getPermutedTotient():
    result = [0, 0, 2]
    for i in range(0, len(primes) - 1):
        prime1 = primes[i]
        for prime2 in primes[i+1:]:
            if (prime1 + prime2) % 9 != 1:
                continue
            n = prime1 * prime2
            if n > limit:
                return result[0]
            phi = (prime1 - 1) * (prime2 - 1)
            ratio = float(n / phi)

            if isPermutation(str(n), str(phi)) and ratio < result[-1]:
                result = [n, phi, ratio]

limit = 10**7
primes = getPrimes(int(1.2 * (limit ** 0.5)))
print (getPermutedTotient())
