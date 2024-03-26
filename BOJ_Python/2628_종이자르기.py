import sys; input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())
arr = [[] for _ in range(2)]
arr = [[0, H], [0, W]]

for _ in range(N):
    d, n = map(int, input().split())
    arr[d].append(n)

arr[0].sort()
arr[1].sort()

# 높이에서 가장 넓은 간격
max_h = 0
for i in range(1, len(arr[0])):
    dist = arr[0][i] - arr[0][i-1]
    if max_h < dist:
        max_h = dist

# 너비에서 가장 넓은 간격
max_w = 0
for i in range(1, len(arr[1])):
    dist = arr[1][i] - arr[1][i-1]
    if max_w < dist:
        max_w = dist

print(max_h * max_w)