def perm(i):
    if i == M:
        print(*p)
        return
    
    for j in range(N):
        if not used[j]:
            p[i] = lst[j]
            used[j] = 1
            perm(i+1)
            used[j] = 0


N, M = map(int, input().split())

lst = list(range(1, N+1))
used = [0] * N
p = [0] * M
perm(0)