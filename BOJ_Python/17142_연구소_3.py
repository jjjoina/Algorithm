import sys; input = sys.stdin.readline
from collections import deque

def find_2():
    lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                lst.append([i, j])

    return lst


def comb(depth, start):
    global ans

    if depth == M:
        rst = bfs()
        if ans > rst:
            ans = rst
        return
    
    for i in range(start, l-M+depth+1):
        vi, vj = virus_lst[i]
        c.append([vi, vj])
        comb(depth+1, i+1)
        c.pop()


def bfs():
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for i, j in c:
        q.append([i, j])
        visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
    
    rst = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0: continue
            if visited[i][j] == -1: return 987654321
            if rst < visited[i][j]:
                rst = visited[i][j]

    return rst


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321
virus_lst = find_2()
l = len(virus_lst)
c = []

comb(0, 0)

print(ans if ans != 987654321 else -1)