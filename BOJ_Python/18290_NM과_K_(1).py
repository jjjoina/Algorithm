# 풀이 2. [60ms] [백트래킹] 다른 사람 풀이 참고
import sys; input = sys.stdin.readline

def comb(n, cur_sum, prev_i, prev_j):
    global ans

    # 가지치기
    if cur_sum + (K-n+1) * 10000 <= ans:
        return
    
    if n == K+1:
        ans = max(ans, cur_sum)
        return
    
    for i in range(prev_i, N):
        if i == prev_i:
            for j in range(prev_j+1, M):
                if used[i][j] == 0:
                    for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < M:
                            used[ni][nj] += 1
                            
                    comb(n+1, cur_sum + arr[i][j], i, j)
                    
                    for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < M:
                            used[ni][nj] -=1
        
        else:
            for j in range(M):
                if used[i][j] == 0:
                    for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < M:
                            used[ni][nj] += 1
                            
                    comb(n+1, cur_sum + arr[i][j], i, j)
                    
                    for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < M:
                            used[ni][nj] -= 1


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

used = [[0] * M for _ in range(N)]
ans = -987654321

comb(1, 0, 0, -1)

print(ans)



# # 풀이 1. [7792ms] 내 풀이
# import sys; input = sys.stdin.readline

# def comb(n, cur_sum, prev_i, prev_j):
#     global ans
    
#     if n == K+1:
#         ans = max(ans, cur_sum)
#         return
    
#     for i in range(prev_i, N):
#         if i == prev_i:
#             for j in range(prev_j+1, M):
#                 if used[i][j] == 0:
#                     for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
#                         ni, nj = i+di, j+dj
#                         if 0 <= ni < N and 0 <= nj < M:
#                             used[ni][nj] += 1
                            
#                     comb(n+1, cur_sum + arr[i][j], i, j)
                    
#                     for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
#                         ni, nj = i+di, j+dj
#                         if 0 <= ni < N and 0 <= nj < M:
#                             used[ni][nj] -=1
        
#         else:
#             for j in range(M):
#                 if used[i][j] == 0:
#                     for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
#                         ni, nj = i+di, j+dj
#                         if 0 <= ni < N and 0 <= nj < M:
#                             used[ni][nj] += 1
                            
#                     comb(n+1, cur_sum + arr[i][j], i, j)
                    
#                     for di, dj in [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]:
#                         ni, nj = i+di, j+dj
#                         if 0 <= ni < N and 0 <= nj < M:
#                             used[ni][nj] -= 1


# N, M, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# used = [[0] * M for _ in range(N)]
# ans = -987654321

# comb(1, 0, 0, -1)

# print(ans)