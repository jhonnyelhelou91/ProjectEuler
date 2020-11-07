def getPrimes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i :: 2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

N = 50 * (10**6)
primes = getPrimes(N)
sums = set()

print ('primes generated')
for p1 in primes:
    if p1 **2 > N:
        break
    for p2 in primes:
        if p1 **2 + p2 ** 3 > N:
            break
        for p3 in primes:
            res = p1**2 + p2**3 + p3**4
            if res < N:
                #print (res, '=', p1, '+', p2, '+', p3)
                sums.add(res)
            else:
                break
sums = list(sums)
sums.sort()
print (len(sums))