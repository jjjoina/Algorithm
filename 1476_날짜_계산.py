import sys; input = sys.stdin.readline

E, S, M = map(int, input().split())

ans = 1
e = s = m = 1
while not (e == E and s == S and m == M):
    e += 1
    if e == 16:
        e = 1

    s += 1
    if s == 29:
        s = 1

    m += 1
    if m == 20:
        m = 1

    ans += 1

print(ans)