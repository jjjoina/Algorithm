import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [1] + [0] * M

    for coin in coins:
        for val in range(coin, M + 1):
            dp[val] += dp[val - coin]

    print(dp[M])