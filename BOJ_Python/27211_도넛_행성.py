import sys; input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque()
    q.append([si, sj])
    arr[si][sj] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = (i + di) % N
            nj = (j + dj) % M
            if arr[ni][nj] == 0:
                q.append([ni, nj])
                arr[ni][nj] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(i, j)
            ans += 1

print(ans)