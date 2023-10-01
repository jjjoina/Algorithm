# 풀이 2. [실패] BFS
import sys; input = sys.stdin.readline
from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if (ni, nj) == (N-1, M-1): return


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

ans = 987654321
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            # 사방 중 하나가 0인 벽에 한해 해당 벽을 뚫었다는 가정으로 bfs 실행
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == 0:    # 인접한 칸 중 길인 칸이 있음
                        arr[i][j] = 0       # 벽 부숨
                        visited = [[-1] * M for _ in range(N)]
                        bfs()
                        if visited[N-1][M-1] > 0:
                            ans = min(ans, visited[N-1][M-1])
                        arr[i][j] = 1       # 벽 부숨 취소
                        break

if ans == 987654321: ans = -1
print(ans)



# 풀이 1. [실패]
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(i, j, flag, cnt):
#     global ans

#     if (i, j) == (N-1, M-1):
#         ans = min(ans, cnt)
#         return
    
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
#             visited[ni][nj] = 1     # 여기서 방문체크

#             if flag:    # 벽을 부순 적이 있으면
#                 if arr[ni][nj] == 0:    # 뚫린 길로만 가야함
#                     dfs(ni, nj, 1, cnt+1)
                
#             else:       # 벽을 부순 적이 없으면
#                 if arr[ni][nj] == 1:    # 벽을 부수고 가거나
#                     dfs(ni, nj, 1, cnt+1)
#                 else:                   # 뚫린 길로 가거나
#                     dfs(ni, nj, 0, cnt+1)
            
#             visited[ni][nj] = 0     # 여기서 방문체크 취소


# N, M = map(int, input().split())
# arr = [list(map(int, input().strip())) for _ in range(N)]
# ans = 987654321
# visited = [[0] * M for _ in range(N)]
# visited[0][0] = 1
# dfs(0, 0, 0, 1)

# if ans == 987654321: ans = -1
# print(ans)