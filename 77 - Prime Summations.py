def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


n = 1000
primes = getPrimes(n)
target = 2

while True:
    ways = { 0: 1 }
    for num1 in primes:
        for num2 in range(num1, target + 1):
            if num2 not in ways:
                ways[num2] = 0
            temp = num2 - num1
            if temp not in ways:
                ways[temp] = 0
            
            ways[num2] += ways[temp]
    if ways[target] > 5000:
        print (target, ways[target])
        break
    target += 1