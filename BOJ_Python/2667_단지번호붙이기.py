import sys; input = sys.stdin.readline

def dfs(i, j):
    global cnt
    cnt += 1

    arr[i][j] = 0   # 방문체크

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
            dfs(ni, nj)


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
l = len(ans)
print(l)
for i in range(l): print(ans[i])