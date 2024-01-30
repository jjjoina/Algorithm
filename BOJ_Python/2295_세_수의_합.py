# 풀이 2. O(N^2) | x + y = k - z
import sys; input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]

xy = set()
for x in range(N):
    for y in range(x, N):
        xy.add(lst[x] + lst[y])

ans = 0
for z in range(N):
    for k in range(N):
        kz = lst[k] - lst[z]
        if kz in xy:
            if ans < lst[k]:
                ans = lst[k]

print(ans)



# # 풀이 1. O(N^3) | x + y + z = k
# import sys; input = sys.stdin.readline

# N = int(input())
# lst = [int(input()) for _ in range(N)]
# st = set(lst)

# ans = 0
# for i in range(N):
#     for j in range(i, N):
#         for k in range(j, N):
#             sum_v = lst[i] + lst[j] + lst[k]
#             if sum_v in st:
#                 if ans < sum_v:
#                     ans = sum_v

# print(ans)