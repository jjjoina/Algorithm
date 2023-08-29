N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for a in A:
    if a < X: print(a, end=' ')