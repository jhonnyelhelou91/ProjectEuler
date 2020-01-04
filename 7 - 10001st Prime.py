#https://stackoverflow.com/questions/9625663/calculating-and-printing-the-nth-prime-number
import math
import sys

def nthPrime(n):
    if (n < 2):
        return 2
    if (n == 2):
        return 3
    lnN = math.log(n)
    lnLnN = math.log(lnN)
    limit = (int)(math.floor(n*(lnN + lnLnN)) + 3)
    root = (int)(math.floor(math.sqrt(limit) + 1))
    limit = (int)(math.floor((limit - 1) / 2))
    root = (int)(math.floor(root / 2 - 1))
    count = 1
    sieve = [False] * limit

    for x in range(0, root):
        if (sieve[x] == False):
            count += 1
            p = 2 * x + 3
            for j in range(2 * x * (x + 3) + 3, limit, p):
                sieve[j] = True
    p = root
    while (count < n):
        if (sieve[p] == False):
            count += 1
        p += 1
    return 2 * p + 1

n = 10001
print (nthPrime(n))