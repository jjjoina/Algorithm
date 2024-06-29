import sys; input = sys.stdin.readline

ans = [None]
dp = [1] * 10
for _ in range(64):
    for i in range(1, 10):
        dp[i] += dp[i-1]
    ans.append(dp[-1])

T = int(input())
for _ in range(T):
    n = int(input())
    print(ans[n])