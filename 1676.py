N = int(input())
N_fac = 1
for i in range(1, N+1):
    N_fac *= i
    
ans = 0
while N_fac % 10 == 0:
    N_fac //= 10
    ans += 1
print(ans)