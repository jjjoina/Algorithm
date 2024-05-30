import sys; input = sys.stdin.readline

N = int(input())
F = list(map(int, input().split()))

F.sort()

ans = 0

for j in range(1, N):
    s, e = 0, j
    t = F[j] * 0.9
    while s <= e:
        m = (s+e) // 2
        if F[m] < t:
            s = m + 1
        else:
            e = m - 1

    ans += j - e - 1

print(ans)