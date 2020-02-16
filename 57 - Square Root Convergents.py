def continuedFraction():
    if len(fractions) == 0:
        return [1, 1]
    previous = fractions[-1]
    previousN = previous[0]
    previousD = previous[1]
    n = previousD
    d = previousN + previousD

    return [n + d, d]

n = 1000
fractions = []
result = 0
for i in range(1, n):
    current = continuedFraction()
    fractions.append(current)
    numerator = len(str(current[0]))
    denominator = len(str(current[1]))
    if numerator > denominator:
        result += 1

print (result)