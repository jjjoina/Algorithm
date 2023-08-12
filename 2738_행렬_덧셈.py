N, M = map(int, input().split())
arr_A = [list(map(int, input().split())) for _ in range(N)]
arr_B = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        ans[i][j] = arr_A[i][j] + arr_B[i][j]

for row in ans:
    print(*row)