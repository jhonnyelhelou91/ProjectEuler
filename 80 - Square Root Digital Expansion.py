from decimal import getcontext, Decimal
digits = 100
getcontext().prec = digits + 2

def digitSum(num):
    return sum(map(int, str(num)))

n = 100
result = 0
for i in range(1, n + 1):
    if i ** 0.5 % 1 != 0:
        sqrt = str(Decimal(i).sqrt()).replace('.', '')[:digits]
        result += digitSum(sqrt)

print (result)