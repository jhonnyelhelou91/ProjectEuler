n = 100
ways = [1] + [0] * n

for num in range(1, n):
    for i in range(num, n + 1):
        ways[i] += ways[i - num]

print (ways[n])