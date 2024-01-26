import sys; input = sys.stdin.readline

N = 123456 * 2
is_prime = [1] * (N+1)
for i in range(2, int(N**0.5)+1):
    if is_prime[i] == 1:
        for j in range(i*i, N+1, i):
            is_prime[j] = 0

while True:
    n = int(input())
    
    if n == 0: break
    
    print(sum(is_prime[n+1:2*n+1]))