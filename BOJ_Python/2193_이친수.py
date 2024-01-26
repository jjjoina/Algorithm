N = int(input())

dp = [0, 1]

for _ in range(N-1):
    dp = [dp[0] + dp[1], dp[0]]

print(sum(dp))