# 풀이 2. [52ms] Disjoint Set
import sys; input = sys.stdin.readline

def find_set(v):
    if p[v] == v:
        return v
    
    p[v] = find_set(p[v])
    return p[v]


def union(v, w):
    pv = find_set(v)
    pw = find_set(w)
    if pv > pw:
        p[pv] = pw
    else:
        p[pw] = pv


N = int(input())
M = int(input())
adj_m = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

p = [i for i in range(N+1)]

for v in range(1, N+1):
    for w in range(1, v+1):
        if adj_m[v][w]:
            union(v, w)

s = set()
for city in plan:
    s.add(find_set(city))

if len(s) == 1: print('YES')
else: print('NO')



# # 풀이 1. [72ms] BFS
# import sys; input = sys.stdin.readline
# from collections import deque

# N = int(input())
# M = int(input())
# adj_m = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
# plan = list(map(int, input().split()))

# q = deque([plan[0]])
# visited = [0] * (N+1)
# visited[plan[0]] = 1
# while q:
#     v = q.popleft()
#     for w in range(1, N+1):
#         if adj_m[v][w] and not visited[w]:
#             q.append(w)
#             visited[w] = 1

# ans = 'YES'
# for city in plan:
#     if not visited[city]:
#         ans = 'NO'
#         break

# print(ans)