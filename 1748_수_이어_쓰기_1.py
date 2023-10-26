N = input()

n = len(N)
ans = 0
for i in range(1, n):
    ans += (i * 9 * 10**(i-1))
ans += (n * (int(N) - 10**(n-1) + 1))
print(ans)