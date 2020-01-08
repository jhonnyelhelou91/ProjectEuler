# a < b < c
# a2 + b2 = c2
# a + b + c = 1000 => c = 1000 - a - b
# a2 + b2 = (1000 - a - b)(1000 - a - b)
# a2 + b2 = 1000000 - 1000a - 1000b - 1000a + a2 + ab - 1000b + ab + b2
# 0 = 1000000 - 2000a - 2000b + 2ab
# 2000a + 2000b - 2ab = 1000000 => b(2000 - 2a) = 1000000 - 2000a => b = (1000000 - 2000a) / (2000 - 2a)
# a < b => a + b < 2b => a + b + c < 2b + c => 1000 < 2b + c
# a: 0 - 100

n = 1000
_range = range(1, n)
for a in _range:
    # avoid division by 0
    if (a != 1000):
        b = (1000000 - 2000 * a) / (2000 - 2 * a)
    else:
        b = -1
    if (b > a and b == (int)(b)):
        b = (int)(b)
        c = n - a - b
        if (c > b and c * c == a * a + b * b):
            print (a, ' ', b, ' ', c)
            print (a * b * c)
        b += 1
