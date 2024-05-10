import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

point = [0] * N
point[0] = lst[0]

for i in range(1, N):
    if lst[i]:
        point[i] = point[i-1] + 1

print(sum(point))