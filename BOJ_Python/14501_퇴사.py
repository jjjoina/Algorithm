# 풀이 2. [44ms] DP
import sys; input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i + lst[i][0] - 1 < N:   # 상담이 N일 전에 끝나는 경우
        dp[i] = max(lst[i][1] + dp[i+lst[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])



# # 풀이 1. [52ms] DFS
# import sys; input = sys.stdin.readline

# def dfs(i, cur_sum):
#     '''
#     i일에 시작하는 상담을 한다 vs 안 한다
#     '''
#     global ans

#     if i == N:
#         ans = max(ans, cur_sum)
#         return
    
#     # 안 한다
#     dfs(i+1, cur_sum)

#     # 한다 (상담이 N일 전에 끝나는 경우만)
#     if i + lst[i][0] - 1 < N:
#         dfs(i + lst[i][0], cur_sum + lst[i][1])


# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]

# ans = 0

# dfs(0, 0)

# print(ans)