fibonacciSequence = [0, 1, 1]
def Fibonacci(n):
    if n <= 2:
        return fibonacciSequence[n]
    result = fibonacciSequence[n - 1] + fibonacciSequence[n - 2]
    fibonacciSequence.append(result)
    return result

n = 1000

result = 1
while len(str(fibonacciSequence[-1])) < n:
    result += 1
    Fibonacci(result)

print (result)