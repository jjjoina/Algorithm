import sys; input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    R, S = input().split()
    for c in S:
        print(c * int(R), end='')
    print()