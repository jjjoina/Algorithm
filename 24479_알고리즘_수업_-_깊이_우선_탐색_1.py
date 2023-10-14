import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt

    visited[v] = 1
    rst[v] = cnt
    cnt += 1
    adj_l[v].sort()
    for w in adj_l[v]:
        if not visited[w]:
            dfs(w)


N, M, R = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_l[u].append(v)
    adj_l[v].append(u)

visited = [0] * (N+1)
cnt = 1
rst = [0] * (N+1)
dfs(R)

for i in range(1, N+1):
    print(rst[i])