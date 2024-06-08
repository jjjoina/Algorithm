import sys; input = sys.stdin.readline

def char_to_int(c):
    if c == 'J':
        return 0
    elif c == 'O':
        return 1
    else:
        return 2


M, N = map(int, input().split())
K = int(input())
arr = [[9] * (N+1)] + [[9] + list(map(char_to_int, input().strip())) for _ in range(M)]

ps = [[[0] * 3 for _ in range(N+1)] for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        for k in range(3):
            ps[i][j][k] = ps[i-1][j][k] + ps[i][j-1][k] - ps[i-1][j-1][k]
        ps[i][j][arr[i][j]] += 1
        
for _ in range(K):
    i1, j1, i2, j2 = map(int, input().split())
    print(*[ps[i2][j2][k] - ps[i1-1][j2][k] - ps[i2][j1-1][k] + ps[i1-1][j1-1][k] for k in range(3)])