count = 0

for power in range(1, 100):
    n = 1
    while len(str(n ** power)) <= power:
        if len (str(n ** power)) == power:
            count += 1
        n += 1

print (count)