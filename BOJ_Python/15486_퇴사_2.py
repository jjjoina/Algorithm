import sys; input = sys.stdin.readline

N = int(input())
consultants = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1]

    next_start_day = i + consultants[i][0]

    if next_start_day <= N and dp[i] < consultants[i][1] + dp[next_start_day]:
        dp[i] = consultants[i][1] + dp[next_start_day]

print(dp[0])