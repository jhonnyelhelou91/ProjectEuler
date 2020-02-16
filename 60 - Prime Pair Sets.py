def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def isPrime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def isPairPrime(a, b):
    strA = str(a)
    strB = str(b)
    return isPrime(int(strA + strB)) and isPrime(int(strB + strA))


def getPrimeSet():
    for primeA in primes:
        #print(primeA)
        for primeB in primes:
            if primeA != primeB and isPairPrime(primeA, primeB):
                #print([primeA, primeB])
                for primeC in primes:
                    if primeA != primeC and primeB != primeC and isPairPrime(primeA, primeC) and isPairPrime(primeB, primeC):
                        #print([primeA, primeB, primeC])
                        for primeD in primes:
                            if primeA != primeD and primeB != primeD and primeC != primeD and isPairPrime(primeA, primeD) and isPairPrime(primeB, primeD) and isPairPrime(primeC, primeD):
                                #print([primeA, primeB, primeC, primeD])
                                for primeE in primes:
                                    if primeA != primeE and primeB != primeE and primeC != primeE and primeD != primeE and isPairPrime(primeA, primeE) and isPairPrime(primeB, primeE) and isPairPrime(primeC, primeE) and isPairPrime(primeD, primeE):
                                        return primeA + primeB + primeC + primeD + primeE
    return -1


primes = getPrimes(10000)
primeSet = getPrimeSet()

print(primeSet)
