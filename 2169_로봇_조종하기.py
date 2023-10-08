# 풀이 2. [1404ms] DP
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

# 첫 줄은 따로 초기화
dp[0][0] = arr[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + arr[0][j]

# 둘째 줄부터 dp
for i in range(1, N):
    ltor = [0] * M
    rtol = [0] * M

    # ltor
    ltor[0] = dp[i-1][0] + arr[i][0]        # 첫 원소 초기화
    for j in range(1, M):
        ltor[j] = max(dp[i-1][j], ltor[j-1]) + arr[i][j]

    # rtol
    rtol[M-1] = dp[i-1][M-1] + arr[i][M-1]  # 첫 원소 초기화
    for j in range(M-2, -1, -1):
        rtol[j] = max(dp[i-1][j], rtol[j+1]) + arr[i][j]
    
    # dp i행 채우기
    for j in range(M):
        dp[i][j] = max(ltor[j], rtol[j])

print(dp[N-1][M-1])



# # 풀이 1. [실패] DFS
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(i, j, cur_sum):
#     global ans

#     if (i, j) == (N-1, M-1):
#         ans = max(ans, cur_sum)
#         return
    
#     for di, dj in [[0, 1], [1, 0], [0, -1]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             dfs(ni, nj, cur_sum + arr[ni][nj])  # 다음 값 더하고 입장
#             visited[ni][nj] = 0


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# visited = [[0] * M for _ in range(N)]
# visited[0][0] = 1
# ans = -1000000000
# dfs(0, 0, arr[0][0])

# print(ans)