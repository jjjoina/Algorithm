# 풀이 2. deque
import sys; input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

lst = [i for i in range(N, 0, -1)]
dq = deque(lst)
ans = []

while dq:
    dq.rotate(K)
    ans.append(dq.popleft())

print('<', end='')
for i in range(N-1):
    print(ans[i], end=', ')
print(f'{ans[N-1]}>')



# 풀이 1. [시간 초과]
# import sys; input = sys.stdin.readline

# N, K = map(int, input().split())

# lst = [i for i in range(N)]
# visited = [0] * N
# ans = [K]
# visited[K-1] = 1

# i = K-1
# while len(ans) < N:
#     cnt = 0
#     while cnt < K:
#         i = (i+1) % N
#         if not visited[i]:
#             cnt += 1
#     ans.append(i+1)
#     visited[i] = 1
    
# print('<', end='')
# for i in range(N-1):
#     print(ans[i], end=', ')
# print(f'{ans[N-1]}>')