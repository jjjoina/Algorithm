# 풀이 2. 데이크스트라
import sys; input = sys.stdin.readline
import heapq

def dijkstra(si, sj):
    W = [[987654321] * N for _ in range(N)]
    W[si][sj] = arr[si][sj]
    heap = [(W[si][sj], 0, 0)]  # weight, i, j

    while heap:
        dist, i, j = heapq.heappop(heap)
        if dist == W[i][j]: # 최신 정보면 진행
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < N:
                    if W[ni][nj] > W[i][j] + arr[ni][nj]:   # 갱신이 되는 경우
                        W[ni][nj] = W[i][j] + arr[ni][nj]
                        heapq.heappush(heap, (W[ni][nj], ni, nj))

    return W[N-1][N-1]


tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0: break

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {dijkstra(0, 0)}')



# # 풀이 1. [시간 초과] DFS
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# def dfs(i, j, cost):
#     global ans

#     # 가지치기
#     if cost >= ans:
#         return
    
#     # 도착
#     if (i, j) == (N-1, N-1):
#         ans = cost
#         return
    
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             dfs(ni, nj, cost + arr[ni][nj])
#             visited[ni][nj] = 0


# tc = 0
# while True:
#     tc += 1
#     N = int(input())
#     if N == 0: break

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     visited = [[0] * N for _ in range(N)]
#     visited[0][0] = 1
#     ans = 987654321
#     dfs(0, 0, arr[0][0])

#     print(f'Problem {tc}: {ans}')