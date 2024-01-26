import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def dfs(i, j):
    arr[i][j] = 0   # 방문체크

    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj]:
            dfs(ni, nj)


def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0   # 방문체크

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj]:
                q.append((ni, nj))
                arr[ni][nj] = 0


while True:
    w, h = map(int, input().split())
    if not (w and h): break
    arr = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                # dfs(i, j)
                bfs(i, j)
                ans += 1
    print(ans)