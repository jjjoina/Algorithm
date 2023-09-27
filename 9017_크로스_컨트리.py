import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = [0] * 201
    for i in range(N):
        cnt[lst[i]] += 1

    for i in range(N):
        if cnt[i]
    
    
    print(cnt)