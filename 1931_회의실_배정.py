import sys; input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

j = 0
ans = 1
for i in range(1, N):
    if arr[i][0] >= arr[j][1]:
        j = i
        ans += 1
print(ans)