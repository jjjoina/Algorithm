import sys; input = sys.stdin.readline
from collections import deque

def ans():
    rst = 0
    for i in range(N):
        for j in range(M):
            # 덜 익은 토마토가 있으면 실패
            if arr[i][j] == 0: return -1
            if rst < arr[i][j]: rst = arr[i][j]
    # 정답은 max값 - 1
    return rst - 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# BFS
q = deque()
# 익은 토마토 모두 큐에 넣기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            q.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1

print(ans())