# 풀이 1. [116ms] bisect

import sys; input = sys.stdin.readline
from bisect import bisect_left

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    print(sum(bisect_left(B, a) for a in A))