import sys; input = sys.stdin.readline

arr = [[0] * 100 for _ in range(100)]

N, M = map(int, input().split())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            arr[x][y] += 1
            
ans = 0
for x in range(100):
    for y in range(100):
        if arr[x][y] > M:
            ans += 1
print(ans)