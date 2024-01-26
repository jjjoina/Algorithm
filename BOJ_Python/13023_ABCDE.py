import sys; input = sys.stdin.readline

def dfs(v, depth):
    global flag
    if flag:
        return
    
    if depth == 5:
        flag = 1
        return

    for w in adj_l[v]:
        if not visited[w]:
            visited[v] = 1
            dfs(w, depth+1)
            visited[v] = 0


N, M = map(int, input().split())
adj_l = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

flag = 0
visited = [0] * N

for start in range(N):
    visited[start] = 1
    dfs(start, 1)
    visited[start] = 0
    if flag:
        break

print(flag)