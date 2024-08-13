import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_ = 100
max_ = 1

for i in range(N):
    for j in range(N):
        if min_ > arr[i][j]:
            min_ = arr[i][j]
        if max_ < arr[i][j]:
            max_ = arr[i][j]

ans = 1

for h in range(min_, max_):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] > h and not visited[r][c]:
                cnt += 1
    
                q = deque()
                q.append([r, c])
                visited[r][c] = True

                while q:
                    i, j = q.popleft()
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > h and not visited[ni][nj]:
                            q.append([ni, nj])
                            visited[ni][nj] = True

    if ans < cnt:
        ans = cnt

print(ans)