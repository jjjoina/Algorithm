A, B = map(int, input().split())

A, B = min(A, B), max(A, B)

print(max(B-A-1, 0))
for i in range(A+1, B):
    print(i, end=' ')