# 풀이 2. [44ms] 백트래킹
import sys; input = sys.stdin.readline

def dfs(i, j, prev_dj, cur_sum):
    global ans

    # 가지치기    
    if ans <= cur_sum:
        return

    if i == N:
        ans = cur_sum
        return
    
    for dj in [-1, 0, 1]:
        if dj != prev_dj:
            nj = j + dj
            if 0 <= nj < M:
                dfs(i+1, nj, dj, cur_sum + arr[i][j])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321

for j in range(M):
    dfs(0, j, 9, 0)

print(ans)



# 풀이 1. [44ms] DP
# import sys; input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]

# for j in range(M):
#     dp[0][j] = [arr[0][j]] * 3

# for i in range(1, N):
#     dp[i][0][0] = 987654321
#     dp[i][0][1] = dp[i-1][0][2] + arr[i][0]
#     dp[i][0][2] = min(dp[i-1][1][0], dp[i-1][1][1]) + arr[i][0]

#     for j in range(1, M-1):
#         dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + arr[i][j]
#         dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i][j]
#         dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + arr[i][j]

#     dp[i][M-1][0] = min(dp[i-1][M-2][1], dp[i-1][M-2][2]) + arr[i][M-1]
#     dp[i][M-1][1] = dp[i-1][M-1][0] + arr[i][M-1]
#     dp[i][M-1][2] = 987654321

# ans = 987654321
# for j in range(M):
#     for k in range(3):
#         ans = min(ans, dp[-1][j][k])

# print(ans)