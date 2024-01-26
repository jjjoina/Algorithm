# 풀이 2. DP
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# sum_arr 만들기!!
# sum_arr[i, j] = arr[0][0]부터 arr[i-1][j-1]까지 직사각형 범위의 합
sum_arr = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    # arr[i-1][j-1]부터 arr[x-1][y-1]까지의 부분합?
    # 문제에서 i,j,x,j가 1부터 시작해서 -1씩 해줌
    ans = sum_arr[x][y] - sum_arr[i-1][y] - sum_arr[x][j-1] + sum_arr[i-1][j-1]
    print(ans)


# import sys

# N, M = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# K = int(sys.stdin.readline())
# ans = []
# for _ in range(K):
#     sum_v = 0
#     i, j, x, y = map(int, sys.stdin.readline().split())
#     for row in range(i-1, x):
#         for col in range(j-1, y):
#             sum_v += arr[row][col]
#     ans.append(sum_v)
# for a in ans:
#     print(a)