ans1 = 0
cnt = {}

for _ in range(10):
    n = int(input())
    ans1 += n
    cnt[n] = cnt.get(n, 0) + 1

ans1 //= 10
ans2 = max(cnt.items(), key=lambda x:x[1])[0]

print(ans1)
print(ans2)