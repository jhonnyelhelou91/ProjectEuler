import string

def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def primeFamily(prime, digit, family):
    count = 0
    for _digit in '0123456789':
        n = int(prime.replace(digit, _digit))
        if (n in primes):
            count = count + 1
            #print (n)
    return count == family

n = 8
digitCount = n - 2
repeated = int(digitCount / 2)
print (n, digitCount, repeated)
primes = [p for p in getPrimes(1000000) if len(str(p)) >= digitCount]

for prime in primes:
    primeStr = str(prime)
    index = 0
    
    if (
        (primeStr.count('0') == repeated and primeStr[-1] != '0' and primeFamily(primeStr, '0', n))
        or
        (primeStr.count('1') == repeated and primeStr[-1] != '1' and primeFamily(primeStr, '1', n))
        or
        (primeStr.count('2') == repeated and primeStr[-1] != '2' and primeFamily(primeStr, '2', n))
    ):
        print (prime)
        break