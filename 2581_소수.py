M = int(input())
N = int(input())

min_prime = 0
sum_primes = 0

primes = [0, 0] + [1] * (N-1)
for i in range(2, int(N**0.5)+1):
    for j in range(i*i, N+1, i):
        primes[j] = 0

for i in range(N, M-1, -1):
    if primes[i]:
        sum_primes += i
        min_prime = i

if min_prime:
    print(sum_primes)
    print(min_prime)
else:
    print(-1)