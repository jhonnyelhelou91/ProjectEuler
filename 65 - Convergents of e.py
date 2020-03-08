limit = 100

den = 1
num = 2
for n in range(2, limit + 1):
    if n % 3 == 0:
        a = int(2 * n / 3)
    else:
        a = 1
    prev_den = den
    den = num
    num = a * den + prev_den

string = str(num)
print (string, sum(map(int, string)))
