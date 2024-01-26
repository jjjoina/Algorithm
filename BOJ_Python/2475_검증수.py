arr = list(map(int, input().split()))
ans = 0
for n in arr:
    ans += n**2
print(ans % 10)