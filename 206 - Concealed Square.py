# 1020304050607080900 < x^2 < 192939495969798900
# 1010101010 < x < 1389026623
import math
def is_concealed_square(n):
    number = str(n)
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    num_index = 0
    for digit in range(0, len(number), 2):
        if number[digit] != num[num_index]:
            return False
        num_index += 1
    return True

for x in range(1389026620, 1010101011, -10):
    x2 = x ** 2
    if is_concealed_square(x2):
        print (x, x2)
        break