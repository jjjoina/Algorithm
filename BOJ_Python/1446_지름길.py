import sys; input = sys.stdin.readline

N, D = map(int, input().split())
sc = [(0, 0)]     # shortcuts
for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        sc.append((1, s))
        sc.append((2, e, s, d))

sc.sort(key=lambda x : (x[1], x[0])) # 지점이 같은 경우 시작 지점(1) 먼저 처리

dp = [0] * (D+1)
for i in range(1, len(sc)):
    if sc[i][0] == 1:  # 시작 지점인 경우
        # dp[직전] + 거리차
        dp[sc[i][1]] = dp[sc[i-1][1]] + (sc[i][1] - sc[i-1][1])

    else:   # 끝 지점인 경우
        # min(지금길 탄 경우, 지금길 안 탄 경우)
        # min(dp[출발 지점] + 지름길 길이, dp[직전] + 거리차)
        dp[sc[i][1]] = min(dp[sc[i][2]] + sc[i][3], dp[sc[i-1][1]] + (sc[i][1] - sc[i-1][1]))

# 도착지
dp[D] = dp[sc[-1][1]] + (D - sc[-1][1])

print(dp[-1])