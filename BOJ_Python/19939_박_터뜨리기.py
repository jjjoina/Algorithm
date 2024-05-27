N, K = map(int, input().split())

if N < K*(K+1)//2:
    ans = -1
else:
    if (N - (K-1)*K//2) % K > 0:
        ans = K
    else:
        ans = K-1

print(ans)