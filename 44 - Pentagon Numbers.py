# P(n) = n (3n - 1) / 2 => 2P(n) = 3n2 - n => 3n2 - n - 2P(n) = 0 => n = [-b +/- sqrt(b2 - 4ac)] / 2a
# n = [1 +/- sqrt(1 + 24P(n))] / 6
# for P(n) = 1, n = [1 +/- sqrt(25)] / 6 = (1 +/- 5) = 6 / 6 = 1
# S = P(n) + P(k)
# D = P(n) - P(k)

def pentagonal(n):
    return n * (3 * n - 1) / 2

def isPentagonal(p):
    n = (24 * p + 1) ** 0.5 + 1

    if (n > 0 and n % 6 == 0):
        return True
    return False

check = True
i = 1

while check == True:
    Pi = pentagonal(i)
    for j in range(i - 1, 0, -1):
        Pj = pentagonal(j)
        diff = abs(Pi - Pj)
        if isPentagonal(Pi + Pj) and isPentagonal(diff):
            check = False
            print (i, j, Pi, Pj, diff)
    i += 1