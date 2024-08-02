import sys; input = sys.stdin.readline

N, M, K = map(int, input().split())
adj_d = [{} for _ in range(N + 1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b and adj_d[a].get(b, 0) < c:
        adj_d[a][b] = c

dp = [[-1] * M for _ in range(N + 1)]
dp[1][0] = 0

for v in range(1, N):
    for cnt in range(M - 1):
        if dp[v][cnt] < 0:
            continue

        for w, score in adj_d[v].items():
            dp[w][cnt + 1] = max(dp[w][cnt + 1], dp[v][cnt] + score)

print(max(dp[N]))