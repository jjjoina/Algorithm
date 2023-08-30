import sys; input = sys.stdin.readline

# bfs 돌며 0으로 바꿔두자
def bfs(i, j):
    q = [(i, j)]
    arr[i][j] = 0

    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
                q.append((ni, nj))
                arr[ni][nj] = 0


T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                bfs(i, j)
                ans += 1
    
    print(ans)