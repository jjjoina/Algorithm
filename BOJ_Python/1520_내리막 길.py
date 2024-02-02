# 풀이 2. [1044ms] DP...?
import sys; input = sys.stdin.readline

def solve():
    while True:
        for i in range(N):
            for j in range(M):

                for d in range(4):
                    # 아직 안 채운 방향에 대해
                    if check[i][j][d] == 0:
                        ni, nj = i+di[d], j+dj[d]
                        # 퍼트릴 예정이면 채운다.
                        if arr[i][j] >= arr[ni][nj]:
                            check[i][j][d] = 1
                
                # 다 채워져서 퍼뜨릴 준비가 된 경우
                if sum(check[i][j]) == 4:
                    for d in range(4):
                        ni, nj = i+di[d], j+dj[d]
                        # 아직 퍼뜨리지 않은 방향에 대해
                        if 0 <= ni < N and 0 <= nj < M and check[ni][nj][(d+2)%4] == 0:
                            check[ni][nj][(d+2)%4] = 1  # 퍼뜨림
                            if arr[i][j] > arr[ni][nj]:
                                dp[ni][nj] += dp[i][j]

                    if i == N-1 and j == M-1:
                        return dp[N-1][M-1]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

check = [[[0] * 4 for _ in range(M)] for _ in range(N)]
for j in range(M):
    check[0][j][3] = 1
    check[N-1][j][1] = 1 
for i in range(N):
    check[i][0][2] = 1
    check[i][M-1][0] = 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(solve())



# # 풀이 1. [시간 초과] 완전 탐색
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# def dfs(i, j):
#     global ans
    
#     if (N-1 - i) + (M-1 - j) > arr[i][j] - arr[N-1][M-1]:
#         return

#     if i == N-1 and j == M-1:
#         ans += 1
#         return
    
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < M and arr[i][j] > arr[ni][nj]:
#             dfs(ni, nj)


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 0

# dfs(0, 0)

# print(ans)