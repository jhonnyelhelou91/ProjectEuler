coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200
dp = [0] * (n + 1)
dp[0] = 1
for i in range(0, len(coins)):
    for j in range(coins[i], n + 1):
        dp[j] += dp[j - coins[i]]

print (dp[n])