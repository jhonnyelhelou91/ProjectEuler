def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def isPermutation(a, b):
    if len(a) != len(b):
        return False

    for digit in a:
        if digit not in b:
            return False

    for digit in b:
        if digit not in a:
            return False
    return True

def getPrimePermutations(n):
    valid_primes = []
    for x in primes:
        prime_permutations = [prime for prime in primes if prime > x and isPermutation(str(x), str(prime))]
        for y in prime_permutations:
            prime1 = str(x)
            prime2 = str(y)
            diff = y - x
            valid_primes.append(x)
            if not isPermutation(prime1, prime2):
                break
            valid_primes.append(y)
            for k in range(2, n):
                next_prime = valid_primes[-1] + diff
                if next_prime not in primes or not isPermutation(prime1, str(next_prime)):
                    break
                valid_primes.append(next_prime)
            if len(valid_primes) == n:
                return valid_primes
            else:
                valid_primes = []


n = 3
primes = [p for p in getPrimes(1000000) if p > 1487]

print (getPrimePermutations(n))