import math
def largestPalindrome(n):
    a = (int)(math.pow(10, n-1))
    b = (int)(math.pow(10, n))
    _range = range(a, b)
    _max = 1
    for i in _range:
        for j in _range:
            product = i * j
            productStr = str(product)
            if (productStr == productStr[::-1] and product > _max):
                _max = product
    return _max

print(largestPalindrome(3))