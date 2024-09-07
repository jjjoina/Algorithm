import sys; input = sys.stdin.readline
sys.setrecursionlimit(500 * 500 * 2)

dir4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(i, j):
    if dp[i][j] == -1:
        dp[i][j] = 0

        for di, dj in dir4:
            ni = i + di
            nj = j + dj

            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] > arr[i][j]:
                dp[i][j] += dfs(ni, nj)

    return dp[i][j]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
dp[0][0] = 1

print(dfs(M - 1, N - 1))