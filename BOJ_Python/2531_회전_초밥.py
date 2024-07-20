import sys; input = sys.stdin.readline

N, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(N)]

kind = 1
cnt = [0] * (d+1)
cnt[c] = 1
for i in range(k):
    cnt[lst[i]] += 1
    if cnt[lst[i]] == 1:
        kind += 1
ans = kind

for i in range(N-1):
    old = lst[i]
    new = lst[(i+k) % N]

    cnt[old] -= 1
    if cnt[old] == 0:
        kind -= 1

    cnt[new] += 1
    if cnt[new] == 1:
        kind += 1

    if ans < kind:
        ans = kind

print(ans)