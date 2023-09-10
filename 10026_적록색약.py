import sys; input = sys.stdin.readline
from collections import deque

def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
ans1 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c, arr[r][c])
            ans1 += 1

for r in range(N):
    for c in range(N):
        if arr[r][c] == 'G': arr[r][c] = 'R'

visited = [[0] * N for _ in range(N)]
ans2 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c, arr[r][c])
            ans2 += 1

print(ans1, ans2)