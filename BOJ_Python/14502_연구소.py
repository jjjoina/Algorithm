import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 2
        
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                cnt += 1

    return cnt
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 리스트 만들기
zero_lst = []
len_of_zero_lst = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_lst.append([i, j])
            len_of_zero_lst += 1

# 빈칸에서 3개 조합 고르며 벽 세우기
ans = 0
for first in range(len_of_zero_lst - 2):
    arr[zero_lst[first][0]][zero_lst[first][1]] = 1

    for second in range(first + 1, len_of_zero_lst - 1):
        arr[zero_lst[second][0]][zero_lst[second][1]] = 1

        for third in range(second + 1, len_of_zero_lst):
            arr[zero_lst[third][0]][zero_lst[third][1]] = 1
            
            # 바이러스 퍼트리기
            rst = bfs()
            if ans < rst:
                ans = rst

            arr[zero_lst[third][0]][zero_lst[third][1]] = 0     # 원복
        arr[zero_lst[second][0]][zero_lst[second][1]] = 0       # 원복
    arr[zero_lst[first][0]][zero_lst[first][1]] = 0             # 원복
    
print(ans)