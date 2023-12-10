import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    max_v = -1
    for _ in range(N):
        S, L = input().split()
        L = int(L)
        if L > max_v:
            max_v = L
            ans = S
    
    print(ans)