import sys; input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

ans = -1000
acc = 0     # 누적

for i in range(n):
    acc += lst[i]
    if ans < acc:
        ans = acc
    if acc < 0:
        acc = 0

print(ans)