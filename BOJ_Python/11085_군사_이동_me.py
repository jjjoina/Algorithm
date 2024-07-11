import sys; input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
ways = [list(map(int, input().split())) for _ in range(w)]

group = [i for i in range(p)]

ways.sort(key=lambda x: -x[2])
for s, e, w in ways:
    min_, max_ = sorted([group[s], group[e]])

    for i in range(p):
        if group[i] == max_:
            group[i] = min_

    if group[c] == group[v]:
        print(w)
        break