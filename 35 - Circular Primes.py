import math
def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def getCircularPrimes(n):
    result = [n]
    number = str(n)
    count = len(number)

    while count > 0:
        rotated = int(number[1:] + number[0])
        if (len(number) != len(str(rotated))):
            return []
        number = str(rotated)
        if (rotated not in primes):
            return []
        result.append(rotated)
        count -= 1
    
    return result

n = 1000000
primes = getPrimes(n)
circularPrimes = set()

for prime in primes:
    if (prime not in circularPrimes):
        temp = getCircularPrimes(prime)
        for n in temp:
            circularPrimes.add(n)

print (len(circularPrimes))