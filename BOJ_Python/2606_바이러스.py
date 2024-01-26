from collections import deque

N = int(input())
E = int(input())
adj_l = [[] for _ in range((N+1))]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# BFS
visited = [0] * (N+1)
q = deque()
q.append(1)
visited[1] = 1
while q:
    v = q.popleft()
    for w in adj_l[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = 1

print(visited.count(1) - 1)