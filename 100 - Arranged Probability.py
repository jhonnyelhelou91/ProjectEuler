# B + R = N
# P = B / (R + B) * (B - 1) / (R + B - 1)
# P = B / N * (B - 1) / (N - 1)
# P * N * (N - 1) = B^2 - B
# B^2 - B - (N * (N - 1) * P) = 0
# B^2 - B - (P * N^2) + (P * N) = 0
# for P = 1/2 => B^2 - B - N^2 / 2 + N / 2 = 0
#             => 2 * B ^ 2 - 2 * B - N^2 + N = 0
# Ax2 + Bxy + Cy2 + Dx + Ey + F = 0 => A = -1, B = 0, C = 2, D = 1, E = -2, F = 0
# https://blog.katastros.com/a?ID=01350-3127a765-04db-4606-bf0b-e37692746e8f

MAX = 10**12
x = 21
y = 15

while x<MAX:
    print x,y 
    tmpy = 3*y + 2*x - 2
    tmpx = 4*y + 3*x - 3
    x = tmpx
    y = tmpy

print x, y