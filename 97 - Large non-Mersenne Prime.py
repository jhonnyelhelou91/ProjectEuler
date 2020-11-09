import math
N = 10

_max = math.pow(10, N + 1)
result = 1
for i in range(0, 7830457):
    result = (result * 2) % _max
result *= 28433
result += 1
result %= (_max / 10)

print(result)