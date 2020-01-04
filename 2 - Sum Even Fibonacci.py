# Fn = Fn-1 + Fn-2
# Fx = 4Fx-1 + Fx-2

res = 0
fib = 0
fib0 = 0
fib1 = 2
_max = 4000000

while fib < _max:
    if (fib1 < _max):
        res += fib1
    fib = 4 * fib1 + fib0
    fib0 = fib1
    fib1 = fib

print(res)