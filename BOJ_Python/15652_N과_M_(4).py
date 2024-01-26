def perm(i, prev):
    if i == M:
        print(*p)
        return
    
    for j in range(prev, N+1):
        p.append(j)
        perm(i+1, j)
        p.pop()


N, M = map(int, input().split())
p = []
perm(0, 1)