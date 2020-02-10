_max = 100

factorials = [1]
for x in range(1, _max + 1):
    factorials.append(factorials[-1] * x)

count = 0
for n in range(1, _max + 1):
    for r in range(1, n):
        result = factorials[n] / (factorials[r] * factorials[n - r])
        if (result > 1000000):
            count = count + 1

print (count)