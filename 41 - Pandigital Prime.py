def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def isPandigital(n):
    digits = set()
    for i in n:
        num = int(i)
        if (num in digits or num == 0):
            return False
        digits.add(num)
    for i in range(1, len(n) + 1):
        if (i not in digits):
            return False
    return True

primes = getPrimes(10000000)
primes.reverse()

for prime in primes:
    if (isPandigital(str(prime))):
        print (prime)
        break
