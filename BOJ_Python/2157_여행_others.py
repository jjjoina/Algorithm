import sys; input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
adj_d = [{} for _ in range(N + 1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b and adj_d[a].get(b, 0) < c:
        adj_d[a][b] = c

dp = [[0] * (M + 1) for _ in range(N + 1)]
q = deque()
q.append([1, 1])     # [도시 번호, 경유한 도시 수]

while q:
    v, cnt = q.popleft()

    if cnt == M:
        continue

    for w, score in adj_d[v].items():
        if dp[w][cnt + 1] == 0: # [w, cnt + 1] 쌍을 큐에 한번만 넣기 위함
            q.append([w, cnt + 1])

        dp[w][cnt + 1] = max(dp[w][cnt + 1], dp[v][cnt] + score)

print(max(dp[N]))