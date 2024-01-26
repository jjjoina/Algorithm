import sys; input = sys.stdin.readline
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
for i in range(N):
    A[i] -= B
    if A[i] < 0:
        A[i] = 0
    ans += math.ceil(A[i] / C)

print(ans)