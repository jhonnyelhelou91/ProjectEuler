import itertools

count = 0
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_digit_square(n):
    number = str(n)
    result = 0
    for i in range(0, len(number)):
        digit = int(number[i])
        result += squares[digit]

    return result

def square_chain(n):
    while n != 1 and n != 89:
        n = sum_digit_square(n)
    return n

fact7 = factorial(7)
digits = range(10)

for num in itertools.combinations_with_replacement(digits, 7):
    cur = sum(d**2 for d in num)
    if cur > 0 and square_chain(cur) == 89:
        cnt = fact7
        for _, g in itertools.groupby(num):
            cnt /= factorial(len(list(g)))
        count += cnt
print(count)
