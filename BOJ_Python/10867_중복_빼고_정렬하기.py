import sys; input = sys.stdin.readline

N = int(input())
print(*sorted(set(map(int, input().split()))))