import sys; input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * N for _ in range(N)]
dp[0][0] = True

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            continue

        if i + arr[i][j] < N:
            dp[i + arr[i][j]][j] = True

        if j + arr[i][j] < N:
            dp[i][j + arr[i][j]] = True

print("HaruHaru" if dp[-1][-1] else "Hing")