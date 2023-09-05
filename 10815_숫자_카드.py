import sys; input = sys.stdin.readline

N = int(input())
arr = set(input().split())
M = int(input())
find = input().split()
for n in find:
    print(1 if n in arr else 0, end=' ')