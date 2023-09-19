# 풀이 3. [336ms] BFS with queue
from collections import deque
import sys; input = sys.stdin.readline

N = int(input())
adj_l = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
visited = [0] * (N+1)
parent = [0] * (N+1)

q = deque([1])
visited[1] = 1
while q:
    v = q.popleft()
    for w in adj_l[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = 1
            parent[w] = v

for i in range(2, N+1):
    print(parent[i])



# # 풀이 2. [376ms] DFS with stack
# import sys; input = sys.stdin.readline

# N = int(input())
# adj_l = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)
# visited = [0] * (N+1)
# parent = [0] * (N+1)

# stack = [1]
# visited[1] = 1
# while stack:
#     v = stack.pop()
#     for w in adj_l[v]:
#         if not visited[w]:
#             stack.append(w)
#             visited[w] = 1
#             parent[w] = v

# for i in range(2, N+1):
#     print(parent[i])



# # 풀이 1. [328ms] DFS with recursion
# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(v):
#     visited[v] = 1  # 부모로 되돌아가지 않기 위해 방문 체크

#     for w in adj_l[v]:
#         if not visited[w]:
#             parent[w] = v
#             dfs(w)


# N = int(input())
# adj_l = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)
# visited = [0] * (N+1)
# parent = [0] * (N+1)

# dfs(1)

# for i in range(2, N+1):
#     print(parent[i])