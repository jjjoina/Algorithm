import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
    
q = deque()
visited = [-1] * (N+1)
q.append(1)
visited[1] = 0
while q:
    v = q.popleft()
    for w in adj_lst[v]:
        if visited[w] == -1:
            q.append(w)
            visited[w] = visited[v] + 1

ans_dist = max(visited)
ans_lst = []
for i in range(1, N+1):
    if visited[i] == ans_dist:
        ans_lst.append(i)
ans_num = min(ans_lst)
ans_cnt = len(ans_lst)

print(ans_num, ans_dist, ans_cnt)