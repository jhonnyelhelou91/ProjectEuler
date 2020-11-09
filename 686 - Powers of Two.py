def next_power(l, n):
    powers = 0
    _max = 10 ** len(str(l))
    num = 1
    exponent = 0
    while True:
        if int(num) == l:
            powers += 1
        if powers == n:
            return (exponent, num)

        num *= 2
        while int(num) > _max:
            num /= 10
        exponent += 1


print(next_power(123, 678910))
