import sys; input = sys.stdin.readline

N = int(input())
adj_m = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj_m[i][j] |= adj_m[i][k] & adj_m[k][j]

for row in adj_m:
    print(*row)