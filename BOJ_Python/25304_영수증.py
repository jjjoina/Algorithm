import sys; input = sys.stdin.readline

X = int(input())
N = int(input())
sum_v = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum_v += a * b
if X == sum_v:
    print('Yes')
else:
    print('No')