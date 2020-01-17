def isPandigital(n):
    if len(n) != 9:
        return False
    digits = set()
    for i in n:
        num = int(i)
        if (num in digits or num == 0):
            return False
        digits.add(num)
    for i in range(1, len(n) + 1):
        if (i not in digits):
            return False
    return True
    
def pandigitalMultiple(n, k):
    number = ''
    while k > 0:
        number = str(n * k) + number
        k -= 1

    return number

def getPandigitalMultiple():
    pandigitals = []
    x = 1
    for n in range(2, 9):
        while True:
            pandigital = pandigitalMultiple(x, n)
            if len(str(pandigital)) > 9:
                break
            if isPandigital(pandigital):
                pandigitals.append(pandigital)
            x += 1
    return pandigitals

pandigitals = getPandigitalMultiple()
pandigitals.sort()
print (pandigitals[-1])