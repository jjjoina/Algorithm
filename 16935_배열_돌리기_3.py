import sys; input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ops = list(map(int, input().split()))

for op in ops:
    if op == 1:
        for i in range(N//2):
            arr[i], arr[N-1-i] = arr[N-1-i], arr[i]

    elif op == 2:
        for i in range(N):
            for j in range(M//2):
                arr[i][j], arr[i][M-1-j] = arr[i][M-1-j], arr[i][j]

    elif op == 3:
        tmp = [[0] * N for _ in range(M)]
        for i in range(N):
            for j in range(M):
                tmp[j][N-1-i] = arr[i][j]
        arr = tmp
        N, M = M, N

    elif op == 4:
        tmp = [[0] * N for _ in range(M)]
        for i in range(N):
            for j in range(M):
                tmp[M-1-j][i] = arr[i][j]
        arr = tmp
        N, M = M, N

    elif op == 5:
        tmp = [[0] * M for _ in range(N)]
        for i in range(N//2):
            tmp[i] = arr[N//2 + i][:M//2] + arr[i][:M//2]
            tmp[N//2 + i] = arr[N//2 + i][M//2:] + arr[i][M//2:]
        arr = tmp
    
    else:
        tmp = [[0] * M for _ in range(N)]
        for i in range(N//2):
            tmp[i] = arr[i][M//2:] + arr[N//2 + i][M//2:]
            tmp[N//2 + i] = arr[i][:M//2] + arr[N//2 + i][:M//2]
        arr = tmp

for row in arr:
    print(*row)