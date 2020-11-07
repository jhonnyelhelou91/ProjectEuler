# https://cat100percentile.com/2013/09/26/shortest-path-cuboid/
# given a cuboid with sizes (a, b, c) where 1 < a < b < c, the shortest path would be: sqrt((a + b)^2 + c^2)

import math

def isShortestPath(a, b, c):
    return math.sqrt((b + c)**2 + a**2) % 1 == 0

L = 1000000
count = 0
a = 2

while count < L:
    a += 1
    for bc in range(3, 2*a):
        if (bc*a) % 12 == 0:
            s = math.sqrt(bc*bc + a*a)
            if not s % 1:
                count += min(bc, a+1) - (bc+1)//2

print (a, count)