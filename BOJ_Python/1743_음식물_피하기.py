import sys; input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    size = 1

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = True
                size += 1

    return size


N, M, K = map(int, input().split())
arr = [[False] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = True

visited = [[False] * M for _ in range(N)]
ans = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] and not visited[r][c]:
            size = bfs(r, c)
            if ans < size:
                ans = size

print(ans)