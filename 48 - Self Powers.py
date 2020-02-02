n = 1000
digits = 10
limit = 10 ** 10
result = 0

for x in range(1, n):
    number = (x ** x) % limit
    result += number

print (result % limit)