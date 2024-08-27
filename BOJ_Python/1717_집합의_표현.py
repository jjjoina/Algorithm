import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(u, v):
    pu = find(u)
    pv = find(v)
    parent[pv] = pu


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, input().split())
    
    if c == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')