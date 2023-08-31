N, B = map(int, input().split())
ans = ''
while N:
    r = N % B
    if r >= 10:
        r = chr(ord('A') + (r-10))
    else:
        r = str(r)
    ans += r
    N //= B
print(ans[::-1])