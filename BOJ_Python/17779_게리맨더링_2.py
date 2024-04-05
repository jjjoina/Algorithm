# 풀이 2. [244ms] 경계 그리지 않음
import sys; input = sys.stdin.readline
from collections import deque

def calculate(x, y, d1, d2):
    population = [0] * 5

    # 구역 0 인구 수 구하기
    c = y
    for r in range(x+d1):
        if r >= x:
            c -= 1
        population[0] += sum(arr[r][:c+1])

    # 구역 1 인구 수 구하기
    c = y + 1
    for r in range(x+d2+1):
        if r >= x+1:
            c += 1
        population[1] += sum(arr[r][c:])
    
    # 구역 2 인구 수 구하기
    c = y - d1 - 1 - 1
    for r in range(x+d1, N):
        if r <= x+d1+d2:
            c += 1
        population[2] += sum(arr[r][:c+1])
    
    # 구역 3 인구 수 구하기
    c = y + d2 + 1
    for r in range(x+d2+1, N):
        if r <= x+d1+d2+1:
            c -= 1
        population[3] += sum(arr[r][c:])
    
    # 구역 4 인구 수 구하기
    population[4] = sum_v - sum(population[:4])
    
    # print(population)

    return max(population) - min(population)
            

def divide():
    global ans

    for x in range(N-2):
        for y in range(1, N-1):
            max_d1 = y
            for d1 in range(1, max_d1+1):
                max_d2 = min(N-x-d1-1, N-y-1)
                for d2 in range(1, max_d2+1):
                    # print(f'x = {x}, y = {y}, d1 = {d1}, d2 = {d2}')
                    rst = calculate(x, y, d1, d2)
                    # print(f'rst = {rst}')
                    # print()
                    if ans > rst:
                        ans = rst
                    if ans == 0:
                        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_v = sum(map(sum, arr))

ans = 987654321
divide()

print(ans)



# # 풀이 1. [3416ms] 경계 그림
# import sys; input = sys.stdin.readline
# from collections import deque

# def calculate(x, y, d1, d2):
#     populations = [0] * 5
#     visited = [[-1] * N for _ in range(N)]

#     # 4 경계
#     for dd1 in range(d1):
#         visited[x + dd1][y - dd1] = 4
#         populations[4] += arr[x + dd1][y - dd1]

#         visited[x+d1+d2 - dd1][y-d1+d2 + dd1] = 4
#         populations[4] += arr[x+d1+d2 - dd1][y-d1+d2 + dd1]
    
#     for dd2 in range(d2):
#         visited[x+d1 + dd2][y-d1 + dd2] = 4
#         populations[4] += arr[x+d1 + dd2][y-d1 + dd2]

#         visited[x+d2 - dd2][y+d2 - dd2] = 4
#         populations[4] += arr[x+d2 - dd2][y+d2 - dd2]

#     # 0 경계
#     for r in range(x):
#         visited[r][y] = 0
#         populations[0] += arr[r][y]
#     for c in range(y-d1):
#         visited[x+d1-1][c] = 0
#         populations[0] += arr[x+d1-1][c]

#     # 1 경계
#     for r in range(x+1):
#         visited[r][y+1] = 1
#         populations[1] += arr[r][y+1]
#     for c in range(y+d2+1, N):
#         visited[x+d2][c] = 1
#         populations[1] += arr[x+d2][c]

#     # 2 경계
#     for r in range(x+d1+d2, N):
#         visited[r][y-d1+d2-1] = 2
#         populations[2] += arr[r][y-d1+d2-1]
#     for c in range(y-d1):
#         visited[x+d1][c] = 2
#         populations[2] += arr[x+d1][c]

#     # 3 경계
#     for r in range(x+d1+d2+1, N):
#         visited[r][y-d1+d2] = 3
#         populations[3] += arr[r][y-d1+d2]
#     for c in range(y+d2, N):
#         visited[x+d2+1][c] = 3
#         populations[3] += arr[x+d2+1][c]

#     # 0, 1, 2, 3 채우기
#     q = deque()
#     q.append([0, 0])
#     q.append([0, N-1])
#     q.append([N-1, 0])
#     q.append([N-1, N-1])
#     visited[0][0] = 0
#     visited[0][N-1] = 1
#     visited[N-1][0] = 2
#     visited[N-1][N-1] = 3
#     while q:
#         i, j = q.popleft()
#         populations[visited[i][j]] += arr[i][j]
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
#                 q.append([ni, nj])
#                 visited[ni][nj] = visited[i][j]

#     # 4 채우기
#     for r in range(N):
#         for c in range(N):
#             if visited[r][c] == -1:
#                 visited[r][c] = 4
#                 populations[4] += arr[r][c]
    
#     # print(populations)
#     # for row in visited: print(*row)

#     return max(populations) - min(populations)
            

# def divide():
#     global ans

#     for x in range(N-2):
#         for y in range(N-2):
#             max_d1 = y
#             for d1 in range(1, max_d1+1):
#                 max_d2 = min(N-x-d1-1, N-y-1)
#                 for d2 in range(1, max_d2+1):
#                     # print(f'x = {x}, y = {y}, d1 = {d1}, d2 = {d2}')
#                     rst = calculate(x, y, d1, d2)
#                     # print(rst)
#                     # print()
#                     if ans > rst:
#                         ans = rst
#                     if ans == 0:
#                         return


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 987654321
# divide()

# print(ans)