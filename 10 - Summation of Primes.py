def sumPrimes(n):
    sieves = [0] * n
    _sum = 0

    for i in range(2, n):
        if (sieves[i] == 0):
            sieves[i] = 1
            for k in range(i + i, n, i):
                sieves[k] = -1
            if (sieves[i] == 1):
                _sum += i
    return _sum

print (sumPrimes(2000000))