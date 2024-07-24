import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, w):
    pv = find(v)
    pw = find(w)
    if pv < pw:
        parent[w] = pv
    else:
        parent[v] = pw


N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]

lectures.sort(key=lambda x: -x[0])  # 강연료 내림차순 정렬
max_d = max(d for p, d in lectures) if N else 0
parent = [i for i in range(max_d+1)]
ans = 0

for p, d in lectures:
    pd = find(d)
    if pd > 0:
        ans += p
        union(pd, pd-1)

print(ans)