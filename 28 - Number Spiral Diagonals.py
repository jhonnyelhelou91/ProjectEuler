n = 1001
spiralIndex = 1
last = n ** 2
sumDiagonals = 1
value = 1

while value < last:
    step = 2 * spiralIndex
    for diagonal in [1, 2, 3, 4]:
        value += step
        sumDiagonals += value
    spiralIndex += 1

print (sumDiagonals)