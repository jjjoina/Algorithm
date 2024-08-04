import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append([0, 0])
    visited[0][0] = True

    while q:
        i, j = q.popleft()

        for di, dj in [[0, arr[i][j]], [arr[i][j], 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == -1:
                    return "HaruHaru"
                q.append([ni, nj])
                visited[ni][nj] = True

    return "Hing"


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs())