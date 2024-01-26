N, K = map(int, input().split())
a = b = 1
for i in range(K):
    a *= (N-i)
    b *= (K-i)
print(a//b)