import sys; input = sys.stdin.readline

MAX = 10001

n, k = map(int, input().split())

dp = [0] + [MAX] * k

for _ in range(n):
    coin = int(input())
    
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != MAX else -1)