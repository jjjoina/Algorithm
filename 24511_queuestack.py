# 풀이 2. [정답]

import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))     # 큐 or 스택
B = list(map(int, input().split()))     # A[i]에 들어있는 원소

M = int(input())
C = list(map(int, input().split()))

arr = []
# 큐에 담긴 것들만 끝에서부터 수집
for i in range(N-1, -1, -1):
    if not A[i]:
        arr.append(B[i])
# C 이어 붙이기
arr += C

print(*arr[:M])


# # 풀이 1. [시간초과]

# import sys; input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))     # 큐 or 스택
# B = list(map(int, input().split()))     # A[i]에 들어있는 원소

# M = int(input())
# C = list(map(int, input().split()))

# for c in C:
#     x = c
#     for i in range(N):
#         if A[i] == 0:   # 큐인 경우
#             B[i], x = x, B[i]
#     print(x, end=' ')