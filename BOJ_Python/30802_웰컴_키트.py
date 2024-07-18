import sys; input = sys.stdin.readline
import math

N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())

ans1 = 0
for t in lst:
    ans1 += math.ceil(t / T)

print(ans1)
print(N // P, N % P)