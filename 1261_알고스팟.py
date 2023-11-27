# 풀이 2. [76ms] heapq
import sys; input = sys.stdin.readline
import heapq

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

q = []
cnt = [[987654321] * M for _ in range(N)]
heapq.heappush(q, [0, 0, 0])
cnt[0][0] = 0
while q:
    w, i, j = heapq.heappop(q)

    if i == N-1 and j == M-1:
        print(w)
        break

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 0 and w < cnt[ni][nj]:
                heapq.heappush(q, [w, ni, nj])
                cnt[ni][nj] = cnt[i][j]
            elif arr[ni][nj] == 1 and w+1 < cnt[ni][nj]:
                heapq.heappush(q, [w+1, ni, nj])
                cnt[ni][nj] = cnt[i][j] + 1



# # 풀이 1. [224ms] Queue
# import sys; input = sys.stdin.readline
# from collections import deque

# M, N = map(int, input().split())
# arr = [list(map(int, input().rstrip())) for _ in range(N)]

# q = deque()
# cnt = [[987654321] * M for _ in range(N)]
# q.append([0, 0])
# cnt[0][0] = 0
# while q:
#     i, j = q.popleft()
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < M:
#             if arr[ni][nj] == 0 and cnt[i][j] < cnt[ni][nj]:
#                 q.append([ni, nj])
#                 cnt[ni][nj] = cnt[i][j]
#             elif arr[ni][nj] == 1 and cnt[i][j] + 1 < cnt[ni][nj]:
#                 q.append([ni, nj])
#                 cnt[ni][nj] = cnt[i][j] + 1

# print(cnt[N-1][M-1])