import sys; input = sys.stdin.readline

INF = 1_000_001

N = int(input())
A = list(map(int, input().split()))

dp = [0] + [INF] * N
ans = 0

for a in A:
    s, e = 0, ans

    while s <= e:
        m = (s+e) // 2
        if dp[m] >= a:
            e = m - 1
        else:
            s = m + 1
    
    if dp[e+1] > a:
        dp[e+1] = a
        if ans < e + 1:
            ans = e + 1
    # print(dp[1:ans+1])

print(ans)