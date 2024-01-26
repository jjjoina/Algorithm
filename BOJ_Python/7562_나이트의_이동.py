import sys; input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if (ni, nj) == (ei, ej):
                    return


T = int(input())
for t in range(1, T+1):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    bfs(si, sj)
    print(visited[ei][ej] - 1)