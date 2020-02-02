def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def countConsecutivePrimeSum(n):
    _primes = [p for p in primes if p < n]
    for i in range(0, len(_primes)):
        result = 0
        count = 0
        for j in range(i, len(_primes)):
            x = _primes[j]
            if (result == n):
                return count
            if (n == 953):
                print (x)
            result += x
            count += 1
    return 0

n = 100
primes = getPrimes(n)
consecutive_sums = [0]
for p in primes:
    _sum = p + consecutive_sums[-1]
    consecutive_sums.append(_sum)

print (consecutive_sums)
number_of_primes = 0
for i in range(number_of_primes, len(consecutive_sums)):
    for j in range(i - 1 - number_of_primes, -1, -1):
        diff = consecutive_sums[i] - consecutive_sums[j]
        if diff > n:
            break
        if diff in primes:
            number_of_primes = i - j
            result = diff
print (result)