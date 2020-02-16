# n2 + n - 2x = 0 => n = -1 + sqrt(1 + 8x) / 4
def isTriangular(x):
    return (-1 + (8 * x + 1) ** 0.5) % 4 == 0

# 3n2 - n - 2x = 0 => n = 1 + sqrt(1 + 24x) / 6
def isPentagonal(x):
    return (1 + (24 * x + 1) ** 0.5) % 6 == 0

def hexagonal(n):
    return n * (2 * n - 1)

n = 143
while True:
    n += 1
    Hn = hexagonal(n)
    if (isPentagonal(Hn) and isTriangular(Hn)):
        print (Hn)
        break