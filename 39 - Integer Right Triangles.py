# a < b < c
# a + b < 2b
# a + b + c < 2b + c
# p < 2b + c
# c2 = a2 + b2
# a + b + c = p => a = p - b - c
# (a + b + c)(a + b + c) = p2
# a2 + b2 + c2 + ab + ac + ba + bc + ca + cb = p2
# a2 + b2 + c2 + 2ab + 2ac + 2bc = p2
# 2c2 + 2ab + 2ac + 2bc = p2
# c2 + ab + ac + bc = p2 / 2
# c2 + pb - b2 - bc + pc - bc - c2 + bc = p2 / 2
# -b2 - c2 + pb + pc - bc = p2 / 2
def getRightTriangleCount(p):
    a = 1
    maxA = p / 3
    count = 0
    while a < maxA:
        b = a + 1
        while p > a + b:
            c = p - a - b
            if (c > b and c ** 2 == a ** 2 + b ** 2):
                count += 1
            b += 1
        a += 1
    return count

result = 0
result_p = 0

n = 1000
for p in range(1, n):
    count = getRightTriangleCount(p)
    if (result < count):
        result = count
        result_p = p

print (result, result_p)