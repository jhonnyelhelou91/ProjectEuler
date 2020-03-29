# Constraints:
# -------------
# (1) 0 < a < b < c < length
# (2) right angle triangle => a^2 + b^2 = c^2
# (3) length perimeter => a + b + c = length
# Pythagorian Theorem

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

n = 1500000
limit = int(n ** 0.5)
triangles = [0] * n
result = 0

for M in range(2, limit):
    for N in range(1, M):
        if (N + M) % 2 == 1 and gcd(N, M) == 1:
            a = M**2 - N**2
            b = 2 * M * N
            c = M**2 + N**2
            perimeter = a + b + c
            while perimeter <= n:
                triangles[perimeter - 1] += 1
                perimeter += a + b + c

print (len([p for p in triangles if p == 1]))