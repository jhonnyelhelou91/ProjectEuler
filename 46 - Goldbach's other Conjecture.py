def getPrimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i:: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def isComposite(n):
    if (n <= 3):
        return False
    if (n % 2 == 0 or n % 3 == 0):
        return True
    
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
    return False

def getNonGoldbach(n):
    index = 0
    while primes[index] < n:
        number = (n - primes[index]) / 2
        number = number ** 0.5

        if (number % 1 == 0):
            return False
        index += 1
    return True

primes = [p for p in getPrimes(1000000) if p % 2 == 1]
n = 9
while True:
    n += 2
    if (isComposite(n) and getNonGoldbach(n)):
        print (n)
        break