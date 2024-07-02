import sys; input = sys.stdin.readline

N = int(input())
arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

ps = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + arr[i][j]

ans = arr[1][1]
for K in range(1, N+1):
    for i in range(1, N-K+2):
        for j in range(1, N-K+2):
            profit = ps[i+K-1][j+K-1] - ps[i-1][j+K-1] - ps[i+K-1][j-1] + ps[i-1][j-1]
            if ans < profit:
                ans = profit
                
print(ans)