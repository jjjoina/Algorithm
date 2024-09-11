import sys; input = sys.stdin.readline

INF = 1_000_000_000

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

fw = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    fw[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    fw[a][b] = l
    fw[b][a] = l

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

ans = 0

for i in range(1, n + 1):
    cnt = 0

    for j in range(1, n + 1):
        if fw[i][j] <= m:
            cnt += items[j]

    if ans < cnt:
        ans = cnt

print(ans)