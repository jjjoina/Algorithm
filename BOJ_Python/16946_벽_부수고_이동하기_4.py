import sys; input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque()
    walls = set()
    cnt = 1     # 이어져있는 0의 개수
    
    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] > 0:     # 벽을 만난 경우
                    walls.add((ni, nj))
                
                elif visited[ni][nj] == 0:  # 아직 탐색하지 않은 빈 칸을 만난 경우
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                    cnt += 1

    # 이어져있던 0의 개수를 만났던 벽에 카운트
    for w in walls:
        arr[w[0]][w[1]] += cnt


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        print(arr[i][j] % 10, end='')
    print()