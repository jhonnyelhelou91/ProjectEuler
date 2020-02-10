def isPermuted(a, b):
    if len(a) != len(b):
        return False

    for digit in a:
        if digit not in b:
            return False

    for digit in b:
        if digit not in a:
            return False
    return True

def isPermutedMultiple (x, n):
    for multiple in range(2, n):
        if not isPermuted(str(x), str(multiple * x)):
            return False
    return True

x = 1
n = 6
while not isPermutedMultiple(x, n):
    x += 1

print (x)