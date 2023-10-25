# 풀이 2. DP
import sys; input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = arr[0][0]

# 0행 세팅
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + arr[0][j]

# 0열 세팅
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[N-1][M-1])



# # 풀이 1. [시간 초과] DFS
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(i, j, cur_sum):
#     global ans

#     cur_sum += arr[i][j]

#     if (i, j) == (N-1, M-1):
#         ans = max(ans, cur_sum)
#         return
    
#     for ni, nj in [[i+1, j], [i, j+1], [i+1, j+1]]:
#         if 0 <= ni < N and 0 <= nj < M:
#             dfs(ni, nj, cur_sum)


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# dfs(0, 0, 0)

# print(ans)