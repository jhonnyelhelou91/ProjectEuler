n = 100
powers = set()

for a in range(2, n + 1):
    for b in range(2, n + 1):
        powers.add(a**b)

print (len(powers))