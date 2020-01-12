def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = 100
result = factorial(n)
resultStr = str(result)
print (sum(map(int, resultStr)))