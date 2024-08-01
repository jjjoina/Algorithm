import sys; input = sys.stdin.readline

def solve():
    if M < N:
        interval = N
        k = y
        r = x
        q = M
    else:
        interval = M
        k = x
        r = y
        q = N

    while k <= M * N:
        if (k - r) % q == 0:
            return k + 1
        k += interval
    
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    x -= 1
    y -= 1

    print(solve())