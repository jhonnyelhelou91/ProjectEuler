def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def primeDivisorsCount(n):
    divisors = set()
    for x in primes:
        while (n % x == 0):
            n /= x
            divisors.add(x)
        if n == 1:
            break
        if (x > n):
            return 0

    return len(divisors)

n = 4
primes = getPrimes(1000000)
x = 1
for i in range(0, n):
    x *= primes[i]

print (x)
while True:
    numbers = []
    offset = 0
    while offset < n:
        if (primeDivisorsCount(x + offset) != n):
            x = x + offset
            break
        numbers.append(x + offset)
        offset += 1
    if (len(numbers) == n):
        print(numbers)
        break
    x += 1