import sys; input = sys.stdin.readline

def convert(c):
    if c == '0':
        return 0
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


def union(u, v):
    pu = find(u)
    pv = find(v)

    if pu < pv:
        parent[pv] = pu
    else:
        parent[pu] = pv


def kruskal():
    global sum_
    cnt = 0

    for len_, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            sum_ -= len_
            cnt += 1
            if cnt == N - 1:
                break

    if cnt == N - 1:
        return sum_
    else:
        return -1


N = int(input())
edges = []
sum_ = 0
for i in range(N):
    s = input().strip()
    for j in range(N):
        len_ = convert(s[j])
        sum_ += len_
        if i != j and len_ > 0:
            edges.append([len_, i, j])

edges.sort()
parent = [i for i in range(N)]

print(kruskal())