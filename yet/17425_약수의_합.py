MAX = 0
lst = []
for _ in range(int(input())):
    N = int(input())
    lst.append(N)
    if MAX < N:
        MAX = N

g = [0] * (MAX+1)
for i in range(1, MAX+1):
    sum_v = 0
    for d in range(1, int(i**0.5)+1):
        if i % d == 0:
            sum_v += d
            if i//d != d:
                sum_v += i//d
    g[i] = g[i-1] + sum_v

for n in lst:
    print(g[n])