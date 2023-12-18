import sys; input = sys.stdin.readline

while True:
    M, F = map(int, input().split())
    if (M, F) == (0, 0):
        break
    print(M + F)