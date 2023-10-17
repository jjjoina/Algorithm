import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
cheese = 0
while True:
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
    if cnt == 0: break

    cheese = cnt
    time += 1

    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
    
    # 공기와 닿은 치즈 0으로
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j]:
                arr[i][j] = 0
    

print(time)
print(cheese)