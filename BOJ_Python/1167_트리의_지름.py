import sys; input = sys.stdin.readline
sys.setrecursionlimit(200_000)

def traversal(v):
    global ans

    visited[v] = True

    lengths = [0, 0]

    for w, l in adj_l[v]:
        if not visited[w]:
            lengths.append(l + traversal(w))

    lengths.sort(reverse=True)

    rst = lengths[0] + lengths[1]
    if ans < rst:
        ans = rst

    return lengths[0]


V = int(input())

adj_l = [[] for _ in range(V + 1)]

for _ in range(V):
    v, *info = (map(int, input().split()))

    for i in range(0, len(info) - 1, 2):
        adj_l[v].append([info[i], info[i + 1]])

visited = [False] * (V + 1)
ans = 0

traversal(1)

print(ans)