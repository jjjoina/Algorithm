import sys; input = sys.stdin.readline

N, T = map(int, input().split())
units = [list(map(int, input().split())) for _ in range(N)]

# dp[i] = i시간 공부하여 얻을 수 있는 최대 점수
dp = [0] * (T + 1)

for k, s in units:
    for i in range(T, k - 1, -1):
        dp[i] = max(dp[i], dp[i - k] + s)

print(dp[T])