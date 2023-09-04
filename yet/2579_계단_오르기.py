# 풀이 2. DP
import sys; input = sys.stdin.readline




# 풀이 1. [시간 초과] DFS
# import sys; input = sys.stdin.readline

# def dfs(i, point, cnt):
#     global ans

#     # 계단 범위 벗어남
#     if i > N: return

#     # 마지막 계단을 밟음
#     if i == N:
#         ans = max(ans, point)
#         return
    
#     # 다음 계단의 점수를 얻으면서 올라감
#     # 카운트 0, 1일때만 1칸 위 계단 올라갈 수 있음
#     if cnt < 1:
#         dfs(i+1, point + arr[i+1], cnt + 1)
#     dfs(i+2, point + arr[i+2], 0)


# N = int(input())
# arr = [0] + [int(input()) for _ in range(N)] + [0, 0]

# ans = 0
# dfs(0, 0, -1)   # 시작점은 계단에 포함되지 않음
# print(ans)