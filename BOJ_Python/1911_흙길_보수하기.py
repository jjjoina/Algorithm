import sys; input = sys.stdin.readline
import math

N, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(N)]

pools.sort()

end = -1
ans = 0

for s, e in pools:
    if s < end:
        s = end
    l = e - s
    ans += math.ceil(l / L)
    excess = L - (l % L)
    if excess == L:
        excess = 0
    end = e + excess

print(ans)