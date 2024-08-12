import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []

for i in range(N):
    dp.append(1)
    for j in range(i):
        if A[i] < A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))