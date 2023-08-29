import sys; input = sys.stdin.readline

max_v = 0
max_i = 0
for i in range(1, 10):
    n = int(input())
    if max_v < n:
        max_v = n
        max_i = i
print(max_v)
print(max_i)