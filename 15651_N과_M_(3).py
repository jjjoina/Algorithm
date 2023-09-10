def pwr(j):
    if j == M:
        print(*p)
        return

    for i in range(1, N+1):
        p.append(i)
        pwr(j+1)
        p.pop()


N, M = map(int, input().split())
p = []
pwr(0)