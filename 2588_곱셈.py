A = int(input())
B = int(input())
ans = 0
cnt = 0
while B > 0:
    print(A * (B%10))
    ans += A * (B%10) * (10 ** cnt)
    B //= 10
    cnt += 1
print(ans)