import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
# 목표지점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 0
# BFS
while q:
    i, j = q.popleft()
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] == 1:
            q.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1

for row in visited:
    print(*row)