# 풀이 3. [정답] [932ms] dp
import sys; input = sys.stdin.readline

N = int(input())
dp = [0, 0] + [N+1] * (N-1)    # 초기화

for i in range(1, N+1):
    for j in [2*i, 3*i, i+1]:
        if j <= N:
            dp[j] = min(dp[j], dp[i]+1)

print(dp[N])



# # 풀이 2. [정답] [796ms] BFS, 바텀업, 가지치기(?)
# import sys; input = sys.stdin.readline
# from collections import deque

# N = int(input())

# visited = [0] * (N+1)
# q = deque()
# q.append(1)
# visited[1] = 1
# while q:
#     x = q.popleft()
#     if x == N: break
#     for nx in [3*x, 2*x, x+1]:
#         if nx <= N and not visited[nx]:
#             q.append(nx)
#             visited[nx] = visited[x] + 1

# print(visited[N] - 1)



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