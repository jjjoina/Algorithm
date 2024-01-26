import sys; input = sys.stdin.readline

n = int(input())
for _ in range(n):
    max_C, ans = 0, ''
    p = int(input())
    for _ in range(p):
        C, name = input().split()
        C = int(C)
        if max_C < C:
            max_C, ans = C, name

    print(ans)