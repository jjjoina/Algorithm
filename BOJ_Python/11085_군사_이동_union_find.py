import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(u, v):
    find(u)
    find(v)
    parent[parent[v]] = parent[u]


p, w = map(int, input().split())
c, v = map(int, input().split())
ways = [list(map(int, input().split())) for _ in range(w)]

parent = [i for i in range(p)]
ways.sort(key=lambda x: -x[2])

for s, e, w in ways:
    union(s, e)

    if find(c) == find(v):
        print(w)
        break