import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [[1] * 2 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if lst[j] < lst[i] and dp[j][0] >= dp[i][0]:
            dp[i][0] = dp[j][0] + 1

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if lst[i] > lst[j] and dp[j][1] >= dp[i][1]:
            dp[i][1] = dp[j][1] + 1

print(max(sum(dp[i]) for i in range(N)) - 1)