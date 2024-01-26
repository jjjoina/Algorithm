def perm(k):
    if k == M:
        print(*p)
        return

    for n in lst:
        if n not in p:
            p.append(n)
            perm(k+1)
            p.pop()

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

p = []
perm(0)