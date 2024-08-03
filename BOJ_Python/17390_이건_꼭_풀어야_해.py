import sys; input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ps = [0]
for i in range(N):
    ps.append(ps[i] + A[i])

for _ in range(Q):
    L, R = map(int, input().split())
    print(ps[R] - ps[L - 1])