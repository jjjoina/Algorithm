import sys; input = sys.stdin.readline
from collections import deque

def solve():
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'I':
                bfs(r, c)
                return
            
            
def bfs(si, sj):
    global ans

    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X' and visited[ni][nj] == 0 :
                q.append([ni, nj])
                visited[ni][nj] = 1

                if arr[ni][nj] == 'P':
                    ans += 1


N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

ans = 0
solve()
print(ans if ans > 0 else 'TT')