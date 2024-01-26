ans = [0] * 10001

for i in range(1, 10001):
    if ans[i] == 1: continue

    m = i
    while True:
        tmp = m
        while m:
            tmp += m % 10
            m //= 10
        m = tmp
        if m > 10000:
            break
        ans[m] = 1

    print(i)