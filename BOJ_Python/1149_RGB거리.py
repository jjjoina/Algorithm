# 풀이 2. DP
import sys; input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        arr[i][j] = min([arr[i-1][k] for k in {0, 1, 2}-{j}]) + arr[i][j]
print(min(arr[N-1]))



# # 풀이 1. [시간 초과] backtracking
# import sys; input = sys.stdin.readline

# def dfs(i, prev_color, cur_cost):
#     # i번째 집의 비용을 결정하는 함수
#     global ans
    
#     # 가지치기
#     if ans <= cur_cost: return
    
#     # 종료 조건
#     if i == N+1:
#         ans = cur_cost
#         return
    
#     for color in range(3):
#         if color != prev_color:
#             dfs(i+1, color, cur_cost + arr[i][color])
    
    
# N = int(input())
# arr = [0] + [list(map(int, input().split())) for _ in range(N)]
# ans = 987654321
# dfs(1, -1, 0)
# print(ans)