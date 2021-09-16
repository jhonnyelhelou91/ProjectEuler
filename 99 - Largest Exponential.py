# a^b < c^d => b*ln(a) < d * ln(c)
import math

exponents = [exp.split(',') for exp in open('p099_base_exp.txt', 'r').read().split('\n')]
counter = 0
result = [0, 0]
_line = -1
_max = 1

for exp in exponents:
    a = int(exp[0])
    b = int(exp[1])
    counter += 1
    
    res = b * math.log(a)
    if (res > _max):
        _line = counter
        _max = res
        result = [a, b]

print (result, _max, _line, counter)