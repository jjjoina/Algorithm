import sys; input = sys.stdin.readline
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

l = min(A) * math.ceil(M / N)
r = max(A) * math.ceil(M / N)

while l <= r:
    m = (l + r) // 2    # 시간

    balloons = sum(m // a for a in A)   # m분 동안 만들 수 있는 풍선의 수

    if balloons >= M:
        r = m - 1
    else:
        l = m + 1

print(l)