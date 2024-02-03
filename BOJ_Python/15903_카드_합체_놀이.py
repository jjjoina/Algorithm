# 풀이 2. [Priority Queue] [Python 56ms, Pypy 220ms] TOP2 O(logn)으로 구하기
import sys; input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
lst = list(map(int, input().split()))
heapq.heapify(lst)

for _ in range(m):
    sum_v = heapq.heappop(lst) + heapq.heappop(lst)
    heapq.heappush(lst, sum_v)
    heapq.heappush(lst, sum_v)

print(sum(lst))


# # 풀이 1. [Python 시간초과, PyPy 148ms] TOP2 O(n)으로 구하기
# import sys; input = sys.stdin.readline

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# for _ in range(m):
#     if lst[0] < lst[1]:
#         min1, min2 = lst[0], lst[1]
#         i1, i2 = 0, 1
#     else:
#         min1, min2 = lst[1], lst[0]
#         i1, i2 = 1, 0

#     for i in range(2, n):
#         if min2 > lst[i]:
#             if min1 > lst[i]:
#                 min1, min2 = lst[i], min1
#                 i1, i2 = i, i1
#             else:
#                 min2 = lst[i]
#                 i2 = i
    
#     lst[i1] = lst[i2] = lst[i1] + lst[i2]

# print(sum(lst))