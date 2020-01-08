collatzSequence = { 1: 1 }

def collatz(n):
    #print (n)
    if n in collatzSequence:
        return collatzSequence[n]

    if (n % 2 == 0):
        collatzSequence[n] = 1 + collatz((int)(n / 2))
    else:
        collatzSequence[n] = 1 + collatz(3 * n + 1)
    return collatzSequence[n]

n = 1000000
for x in range(1, n):
    collatz(x)

res = 0
_max = 0
for key in collatzSequence:
    if (_max < collatzSequence[key]):
        _max = collatzSequence[key]
        res = key

print (res, ' ', _max)