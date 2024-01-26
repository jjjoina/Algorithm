fac = [1] * 31
for i in range(1, 31):
    fac[i] = fac[i-1] * i

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    print(fac[M] // (fac[M-N] * fac[N]))