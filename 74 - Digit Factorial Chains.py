def factorialSum(n):
    digitFactorial = [factorials[int(digit)] for digit in str(n)]
    return sum(digitFactorial)

def factorialChain(n):
    chain = set()
    chain.add(n)

    i = factorialSum(n)
    while i not in chain:
        if i in chainCache:
            chainCache[n] = len(chain) + chainCache[i]
            return chainCache[n]
        chain.add(i)
        i = factorialSum(i)

    chainCache[n] = len(chain)
    return len(chain)

chainCache = {0: 1}
factorials = [1]

for i in range(1, 10):
    factorials.append(factorials[i-1] * i)

n = 1000000

for i in range(10, n):
    factorialChain(i)
print(len([p for p in chainCache if chainCache[p] == 60]))