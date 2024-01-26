import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(i, j):
    global ans
    
    if ans: return
    
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == arr[i][j]:
            if visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni, nj)
                checked[ni][nj] = 1
                visited[ni][nj] = 0
            
            elif visited[i][j] - visited[ni][nj] >= 3:
                ans = True
                return
            

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

checked = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = False

for r in range(N):
    for c in range(M):
        if checked[r][c] == 0:
            dfs(r, c)
            
print('Yes' if ans else 'No')