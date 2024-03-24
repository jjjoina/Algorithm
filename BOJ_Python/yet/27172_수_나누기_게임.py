import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N

for i in range(N):
    for j in range(N):
        if lst[i] % lst[j] == 0:
            ans[i] -= 1
            ans[j] += 1

print(*ans)