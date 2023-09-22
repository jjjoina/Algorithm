import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)] + [[0] * N]
    
    for j in range(1, N):
        arr[0][j] += max(arr[1][j-1], arr[2][j-1])
        arr[1][j] += max(arr[0][j-1], arr[2][j-1])
        arr[2][j] += max(arr[0][j-1], arr[1][j-1])
    
    print(max(arr[0][N-1], arr[1][N-1], arr[2][N-1]))