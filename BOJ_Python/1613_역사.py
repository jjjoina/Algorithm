import sys; input = sys.stdin.readline

def dfs(v):
    if not visited[v]:
        visited[v] = True
        for w in next[v]:
            ans_set[v].add(w)
            ans_set[v].update(dfs(w))

    return ans_set[v]


n, k = map(int, input().split())
next = [[] for _ in range(n+1)]
for _ in range(k):
    v, w = map(int, input().split())
    next[v].append(w)

ans_set = [set() for _ in range(n+1)]
visited = [False] * (n+1)

for v in range(1, n+1):
    if not visited[v]:
        dfs(v)

s = int(input())
for _ in range(s):
    u, v = map(int, input().split())
    if v in ans_set[u]:
        print(-1)
    elif u in ans_set[v]:
        print(1)
    else:
        print(0)