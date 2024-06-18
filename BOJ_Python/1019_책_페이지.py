N = input()
len_N = len(N)
N = int(N)
ans = [[0] * len_N for _ in range(10)]

first = N // (10 ** (len_N-1))
for n in range(1, first):
    ans[n][len_N-1] = 10 ** (len_N-1)
ans[first][len_N-1] = N // (10 ** (len_N-1)) + 1

for i in range(len_N-1, -1, -1):
    for n in range(10):
        q = N // (10 ** (i+1)) * 10 + n
        sta = N // (10**i)
        
        if q < sta:
            coe = N // (10 ** (i+1)) + 1
            if n == 0:
                coe -= 1
            ans[n][i] = coe * (10**i)
        
        elif q > sta:
            coe = N // (10 ** (i+1))
            ans[n][i] = coe * (10**i)
        
        else:
            coe = N // (10 ** (i+1))
            if n == 0:
                coe -= 1
            ans[n][i] = coe * (10**i) + N % (10**i) + 1
        
print(*(sum(ans[n]) for n in range(10)))