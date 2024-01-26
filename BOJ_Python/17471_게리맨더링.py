import sys; input = sys.stdin.readline
from collections import deque

def is_connected(group):
    q = deque([group[0]])
    visited[group[0]] = 1
    while q:
        v = q.popleft()
        for w in adj_l[v]:
            if w in group and not visited[w]:
                q.append(w)
                visited[w] = 1

    for v in group:
        if not visited[v]:
            return False
    return True


N = int(input())
p = [0] + list(map(int, input().split()))
adj_l = [[] for _ in range(N+1)]
for i in range(1, N+1):
    adj_l[i] = list(map(int, input().split()))[1:]

ans = 987654321
for i in range(1, 1<<(N-1)):
    group1 = []
    group2 = []
    for j in range(N):
        if i & (1<<j):
            group1.append(j+1)
        else:
            group2.append(j+1)
    
    visited = [0] * (N+1)

    if is_connected(group1) and is_connected(group2):
        rst = 0
        for i in group1:
            rst += p[i]
        for i in group2:
            rst -= p[i]
        ans = min(ans, abs(rst))

if ans == 987654321:
    ans = -1
print(ans)