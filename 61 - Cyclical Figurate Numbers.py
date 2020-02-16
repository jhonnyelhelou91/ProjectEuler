# n2 + n - 2x = 0 => n = -1 + sqrt(1 + 8x) / 4
def isTriangular(x):
    return (-1 + (8 * x + 1) ** 0.5) % 4 == 0

# n2 = x => n = sqrt(x)
def isSquare(x):
    return x ** 0.5 % 1 == 0

# 3n2 - n - 2x = 0 => n = 1 + sqrt(1 + 24x) / 6
def isPentagonal(x):
    return (1 + (24 * x + 1) ** 0.5) % 6 == 0

# 2n2 - n - x = 0 => n = 1 + sqrt(1 + 8x) / 4
def isHexagonal(x):
    return (1 + (1 + 8 * x) ** 0.5) % 4 == 0

# 5n2 - 3n - 2x = 0 => n = 3 + sqrt(9 + 40x) / 10
def isHeptagonal(x):
    return (3 + (9 + 40 * x) ** 0.5) % 10 == 0

# 3n2 - 2n - x = 0 => n = 2 + sqrt(4 + 12x) / 6
def isOctagonal(x):
    return (2 + (4 + 12 * x) ** 0.5) % 6 == 0

def findNext(end, length):
    for i in range(0, len(numbers)):
        if result[i] == 0:
            for j in range(0, len(numbers[i])):
                if numbers[i][j] not in result and int(numbers[i][j] / digit) == int(result[end] % digit):
                    result[i] = numbers[i][j]
                    if length == len(numbers) - 1 and int(result[-1] / digit) == int(result[i] % digit):
                        return True
                    if findNext(i, length + 1):
                        return True
            result[i] = 0
    return False


n = 4
digit = 10 ** (n/2)
start = 10 ** (n - 1)
end = 10 ** n - 1
triangulars = [p for p in range(start, end) if isTriangular(p)]
squares = [p for p in range(start, end) if isSquare(p)]
pentagonals = [p for p in range(start, end) if isPentagonal(p)]
hexagonals = [p for p in range(start, end) if isHexagonal(p)]
heptagonals = [p for p in range(start, end) if isHeptagonal(p)]
octogonals = [p for p in range(start, end) if isOctagonal(p)]
numbers = [
    triangulars,
    squares,
    pentagonals,
    hexagonals,
    heptagonals,
    octogonals
]

result = [0] * len(numbers)
for i in range(0, len(numbers[-1])):
    result[-1] = numbers[-1][i]
    if findNext(len(numbers) - 1, 1):
        print(result, sum(result))