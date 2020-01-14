def getPrimes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i :: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def getCycle(n):
    a = 10 % n
    first = a
    count = 0

    while True:
        a = a * 10 % n
        count += 1
        if a == first or a == 0:
            return count
n = 1000

primes = getPrimes(n)
result_p = 0
result = 0
for x in primes:
    cycle = getCycle(x)
    if (result < cycle):
        result_p = x
        result = cycle

print ('1 /', result_p, '=>', result)