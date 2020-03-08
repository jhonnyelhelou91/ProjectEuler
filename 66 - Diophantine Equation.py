def getPeriod(n):
    root = int(n ** 0.5)
    m = 0
    d = 1
    a = root
    num = a
    den = 1
    prev_num = 1
    prev_den = 0

    while num * num - n * den * den != 1:
        m = d * a - m
        d = int((n - m * m) / d)
        a = int ((root + m) / d)
 
        prev_prev_num = prev_num
        prev_num = num
        prev_prev_den = prev_den
        prev_den = den

        num = a * prev_num + prev_prev_num
        den = a * prev_den + prev_prev_den

    return [n, num, den]

n = 1000
result = [0, 0, 0]

for d in range(2, n + 1):
    if int(d ** 0.5) ** 2 != d:
        period = getPeriod(d)
        if period[1] > result[1]:
            result = period
        
print (result)