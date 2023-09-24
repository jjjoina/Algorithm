import sys; input = sys.stdin.readline
from collections import deque

def ans():
    max_day = 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:   # 덜 익은 토마토가 남아있는 경우
                    return -1
                max_day = max(max_day, arr[i][j][k])
    
    return max_day - 1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 시작 지점들 큐에 추가
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

# BFS
while q:
    i, j, k = q.popleft()   # 익은 토마토의 좌표
    for di, dj, dk in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
        ni, nj, nk = i+di, j+dj, k+dk
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M: # 인덱스 체크
            if arr[ni][nj][nk] == 0:    # 인접한 칸에 덜 익은 토마토가 있으면
                arr[ni][nj][nk] = arr[i][j][k] + 1
                q.append((ni, nj, nk))

# 정답 출력
print(ans())