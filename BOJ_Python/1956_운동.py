import sys; input = sys.stdin.readline

MAX = 10000 * 400 * 400

V, E = map(int, input().split())
fw = [[MAX] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    fw[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

ans = min(fw[i][i] for i in range(1, V+1))
if ans == MAX:
    ans = -1

print(ans)