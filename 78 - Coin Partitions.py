def pentagonal(n):
    return int(n * (3 * n - 1) / 2)

def pentagonalRange(n):
    p = pentagonal(n)
    return [p, p + n]


n = 1000000
index = 0
p = [1]
sgn = [1, 1, -1, -1]

k = sum([pentagonalRange(p) for p in range(1, 250)], [])

while p[index] > 0:
    index += 1
    i = 0
    px = 0
    while k[i] <= index:
        px += p[index - k[i]] * sgn[i % 4]
        i += 1
    p.append(px % n)

print (index)
