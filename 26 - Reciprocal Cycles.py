def getPrimes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def getCycle(n):
    _hash = {}
    a = 10 % n
    t = 1
    _hash[1] = t

    while _hash[a] == None:
        _hash[a] = t
        a = a * 10 % n
        t += 1
    return t - _hash[a]
n = 10

primes = getPrimes(n)
print(getCycle(7))
result_p = 0
result = 0
for x in primes:
    cycle = getCycle(x)
    if (result < cycle):
        result_p = x
        result = cycle

print (result_p, result)