import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

ans = 2*N*M

for i in range(1, N+1):
    for j in range(1, M+1):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            ans += max(arr[i][j]-arr[ni][nj], 0)

print(ans)