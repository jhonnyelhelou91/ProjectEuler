def isPrime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

n = 10
value = 1
spiralIndex = 0
percentage = 100
primesCount = 0
step = 0

while percentage >= n:
    spiralIndex += 1
    step = 2 * spiralIndex
    allCount = 2 * step + 1
    for diagonal in [1, 2, 3, 4]:
        value += step
        if isPrime(value):
            primesCount += 1
    percentage = 100 * (primesCount / allCount)

print(step + 1, percentage)
