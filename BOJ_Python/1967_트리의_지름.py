import sys; input = sys.stdin.readline
sys.setrecursionlimit(20000)

def traversal(v):
    global ans

    lengths = [0, 0]

    for w, l in adj_l[v]:
        lengths.append(l + traversal(w))

    lengths.sort(reverse=True)
    ans = max(ans, lengths[0] + lengths[1])
    return lengths[0]


n = int(input())

adj_l = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    v, w, l = map(int, input().split())
    adj_l[v].append([w, l])

ans = 0

traversal(1)

print(ans)