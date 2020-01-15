def isPandigital(n):
    digits = set()
    for i in str(n):
        num = int(i)
        if (num in digits or num == 0):
            return False
        digits.add(num)
    if len(digits) != 9:
        return False
    for i in range(1, len(str(n)) + 1):
        if (i not in digits):
            return False
    return True

def isPandigitalProduct(a, b):
    n = a * b
    return isPandigital(int(str(a) + str(b) + str(n)))

result = 0
products = set()
for a in range(1, 100):
    for b in range(100, 2000):
        product = a * b
        if (product not in products and isPandigitalProduct(a, b)):
            result += product
            print (a, b, product)
            products.add(product)

print (result)