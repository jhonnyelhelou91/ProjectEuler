def product_sum(product, _sum, factors, start):
    k = product - _sum + factors
    if k < N:
        if product < dp[k]:
            dp[k] = product
        for i in range(start, N // product*2 + 1):
            product_sum(product * i, _sum + i, factors + 1, i)

N = 12000
if N > 12:
    N += 1
dp = [N**2] * N
product_sum(1, 1, 1, 2)
sums = set(dp[2:])

print (sum(sums))