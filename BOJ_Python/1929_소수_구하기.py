import sys; input = sys.stdin.readline

M, N = map(int, input().split())
primes = [0, 0] + [1] * (N-1)

for i in range(2, int(N**0.5)+1):
    if primes[i]:
        for j in range(i*i, N+1, i):
            primes[j] = 0

for i in range(M, N+1):
    if primes[i]: print(i)