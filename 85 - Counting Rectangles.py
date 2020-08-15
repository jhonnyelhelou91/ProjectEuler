import math

def rectangle_count(a, b):
    return (a * b * (a + 1) * (b + 1)) / 4

def first_rectangle_count(x):
    N = 101
    for a in range(1, N):
        for b in range(1, N):
            if rectangle_count(a, b) >= x:
                return ('res', a, b, a * b)


print (first_rectangle_count(2000000))