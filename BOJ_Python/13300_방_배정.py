import sys; input = sys.stdin.readline
import math

N, K = map(int, input().split())
arr = [[0] * 2 for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1

ans = 0
for y in range(6):
    for s in range(2):
        ans += math.ceil(arr[y][s] / K)

print(ans)