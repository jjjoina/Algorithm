# 풀이 2. [pypy로 성공] [504ms] 색종이 N -> 1

import sys; input = sys.stdin.readline

arr = [[0] * 1001 for _ in range(1001)]
N = int(input())    # N : 색종이의 수
# 색종이 붙이기 (제일 위에 것부터)
papers = [list(map(int, input().split())) for _ in range(N)]

ans = []
for n in range(N-1, -1, -1):
    rst = 0
    i, j, w, h = papers[n]
    for row in range(i, i+w):
        for col in range(j, j+h):
            # 놓여진 색종이가 없는 경우
            if arr[row][col] == 0:
                rst += 1
                # n번째로 놓는 색종이이므로 n 표시
                arr[row][col] = n
    ans.append(rst)

for i in range(N-1, -1, -1):
    print(ans[i])


# # 풀이 1. [pypy로 성공] [960ms] 색종이 1 -> N

# import sys; input = sys.stdin.readline

# arr = [[0] * 1001 for _ in range(1001)]
# N = int(input())    # N : 색종이의 수
# # 색종이 붙이기
# for n in range(1, N+1):
#     i, j, w, h = map(int, input().split())
#     for row in range(i, i+w):
#         for col in range(j, j+h):
#             # n번째로 놓는 색종이이므로 n 표시
#             arr[row][col] = n

# for n in range(1, N+1):
#     ans = 0
#     for i in range(1001):
#         for j in range(1001):
#             if arr[i][j] == n:
#                 ans += 1
#     print(ans)