import sys; input = sys.stdin.readline

dp = [[0] * 2001 for _ in range(11)]

for i in range(2001):
    dp[1][i] = i

for i in range(2, 11):
    for j in range(pow(2, i - 1), 2001):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j // 2]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    print(dp[n][m])