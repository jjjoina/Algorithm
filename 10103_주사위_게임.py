import sys; input = sys.stdin.readline

n = int(input())
cy = sd = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        cy -= b
    elif a > b:
        sd -= a

print(cy)
print(sd)