# numerator / denominator < 1
# (10a + n) / (10n + b) < 1
# (10a + n) < (10n + b) => 10a - 9n - b < 0
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

digits = range(1, 10)
resultNumerator = 1
resultDenominator = 1
for n in digits:
    for a in range(1, n):
        if (n != a):
            for b in digits:
                if (a != b and 10 * a - 9 * n - b):
                    numerator = (10 * a + n)
                    denominator = (10 * n + b)
                    if (a / b == numerator / denominator):
                        resultNumerator *= numerator
                        resultDenominator *= denominator
                        print (numerator, denominator)
common = gcd(resultNumerator, resultDenominator)
print (resultNumerator / common, resultDenominator / common)

