def cal(s, e):
    rs, cs = divmod(s, M)
    re, ce = divmod(e, M)
    dp = [[1] * (ce-cs+1) for _ in range(re-rs+1)]

    for r in range(1, re-rs+1):
        for c in range(1, ce-cs+1):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[-1][-1]


N, M, K = map(int, input().split())

if K > 0:
    print(cal(0, K-1) * cal(K-1, N*M-1))
else:
    print(cal(0, N*M-1))