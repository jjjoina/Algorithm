# 풀이 2. [396ms] 이분 탐색 구현

import sys; input = sys.stdin.readline
from bisect import bisect_left

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    ans = 0

    for a in A:
        l = 0
        r = M - 1

        while l <= r:
            m = (l + r) // 2

            if B[m] >= a:
                r = m - 1
            else:
                l = m + 1

        ans += l

    print(ans)