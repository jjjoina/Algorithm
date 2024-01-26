import sys; input = sys.stdin.readline

def bfs(i, j):
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        
        if (i, j) == (N-1, M-1):
            break
        
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M\
                and arr[ni][nj] and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])