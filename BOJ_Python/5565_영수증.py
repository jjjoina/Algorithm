import sys; input = sys.stdin.readline

sum_v = int(input())
print(sum_v - sum([int(input()) for _ in range(9)]))