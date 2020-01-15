import sys

def getSieve(n):
    sieves = [None] * n
    sieves[1] = False

    for i in range(2, n):
        if (sieves[i] == None):
            sieves[i] = True
            for k in range(i + i, n, i):
                sieves[k] = False
    return sieves

def isTruncatablePrime(n):
    count = len(str(n)) - 1
    div = 10
    while count > 0:
        right = n % div
        left = int (n / div)
        if (sieves[right] == False or sieves[left] == False):
            return False
        count -= 1
        div *= 10
    return True

n = 11
sieves = getSieve(1000000)
result = 0
x = 11
while n > 0:
    x += 2
    if (sieves[x] == True and isTruncatablePrime(x)):
        print ('#', n, ':', x)
        result += x
        n -= 1

print (result)