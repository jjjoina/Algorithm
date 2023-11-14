A, B, C = map(int, input().split())
D = int(input())

A += D // 3600
D %= 3600

B += D // 60
C += D % 60

if C >= 60:
    B += C // 60
    C %= 60

if B >= 60:
    A += B // 60
    B %= 60

A %= 24

print(A, B, C)