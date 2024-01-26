import sys; input = sys.stdin.readline

is_prime = [1] * 1000001
is_prime[0] = is_prime[1] = 0
for i in range(2, 1001):
    if is_prime[i] == 1:
        for j in range(i*i, 1000001, i):
            is_prime[j] = 0

for _ in range(int(input())):
    N = int(input())
    ans = 0
    for i in range(2, N//2 + 1):
        if is_prime[i] == 1 and is_prime[N-i] == 1:
            ans += 1
    print(ans)