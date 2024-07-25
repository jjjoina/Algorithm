import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    elif pu < pv:
        parent[pv] = pu
    else:
        parent[pu] = pv
    return True


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
cnt = 0
ans = sum(e[2] for e in edges)

for u, v, w in edges:
    if union(u, v):
        ans -= w
        cnt += 1
        if cnt == N-1:
            break

for v in range(1, N+1):
    if find(v) != 1:
        ans = -1
        break

print(ans)