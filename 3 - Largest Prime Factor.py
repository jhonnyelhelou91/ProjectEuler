def largestPrimeFactor(n):
    res = 1
    for x in range(2, n):
        if (n % x == 0):
            res = n
            n /= x
            if (n == 1):
                return res
    
    return res

print (largestPrimeFactor(600851475143))