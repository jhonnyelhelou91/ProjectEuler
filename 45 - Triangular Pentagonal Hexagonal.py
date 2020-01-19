def isTriangular(x):
    return (8 * x + 1 ) ** 0.5 % 1 == 0

def isPentagonal(p):
    n = (24 * p + 1) ** 0.5 + 1

    if (n > 0 and n % 6 == 0):
        return True
    return False

def hexagonal(n):
    return n * (2 * n - 1)

n = 143
while True:
    n += 1
    Hn = hexagonal(n)
    if (isPentagonal(Hn) and isTriangular(Hn)):
        print (Hn)
        break