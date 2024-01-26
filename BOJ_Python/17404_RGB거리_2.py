import sys; input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[987654321] * 3 for _ in range(3)] for _ in range(N)]
for j in range(3):
    dp[0][j][j] = arr[0][j]

for i in range(1, N):
    dp[i] = [
        [min(dp[i-1][1][k], dp[i-1][2][k]) + arr[i][0] for k in range(3)],
        [min(dp[i-1][0][k], dp[i-1][2][k]) + arr[i][1] for k in range(3)],
        [min(dp[i-1][0][k], dp[i-1][1][k]) + arr[i][2] for k in range(3)]
    ]

ans = 987654321
for j in range(3):
    for k in range(3):
        if j != k:
            if ans > dp[N-1][j][k]:
                ans = dp[N-1][j][k]

print(ans)