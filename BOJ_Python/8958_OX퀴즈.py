T = int(input())
for t in range(1, T+1):
    arr = input()
    ans = 0
    cnt = 0
    for c in arr:
        if c == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)