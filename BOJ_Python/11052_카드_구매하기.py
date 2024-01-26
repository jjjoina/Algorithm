import sys; input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = max([P[i]] + [dp[j] + dp[i-j] for j in range(1, N//2+1)])

print(dp[N])