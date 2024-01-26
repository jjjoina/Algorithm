T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    ans = a % 10
    r = [ans]
    for _ in range(b-1):
        ans *= a
        ans %= 10
        if ans in r: break
        else: r.append(ans)
    i = b % len(r) - 1
    if r[i] == 0: r[i] = 10
    print(r[i])