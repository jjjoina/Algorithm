import sys; input = sys.stdin.readline

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

adj_cnts = [0] * (N+1)
for u, v in edges:
    adj_cnts[u] += 1
    adj_cnts[v] += 1

d = 0
for u, v in edges:
    d += (adj_cnts[u] - 1) * (adj_cnts[v] - 1)

g = 0
for v in range(1, N+1):
    if adj_cnts[v] >= 3:
        g += adj_cnts[v] * (adj_cnts[v] - 1) * (adj_cnts[v] - 2) // 6

if d > 3 * g:
    print('D')
elif d < 3 * g:
    print('G')
else:
    print('DUDUDUNGA')