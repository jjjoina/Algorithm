import sys; input = sys.stdin.readline

MAX = 100000
Q = 1000000009

dp = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
for i in range(4, MAX+1):
    dp.append([
        (dp[i-1][1] + dp[i-1][2]) % Q,
        (dp[i-2][0] + dp[i-2][2]) % Q,
        (dp[i-3][0] + dp[i-3][1]) % Q
    ])
    
T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % Q)