# 풀이 2.




# # 풀이 1. [시간 초과] BFS
# import sys; input = sys.stdin.readline
# from collections import deque

# N = int(input())

# # BFS
# q = deque([(N, 0)]) # 현재 수, 연산 횟수

# while q:
#     n, cnt = q.popleft()
    
#     if n == 1:
#         print(cnt)
#         break

#     if n % 3 == 0: q.append((n//3, cnt+1))
#     if n % 2 == 0: q.append((n//2, cnt+1))
#     q.append((n-1, cnt+1))