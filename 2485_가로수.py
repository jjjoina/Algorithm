import sys; input = sys.stdin.readline

# 간격들의 최대공약수에 맞춰보자

N = int(input())
arr = [int(input()) for _ in range(N)]

intervals = [arr[i]-arr[i-1] for i in range(1, N)]  # N-1개
gcd = intervals[0]
for i in range(1, N-1):
    a, b = max(gcd, intervals[i]), min(gcd, intervals[i])
    while b > 0:
        a, b = b, a%b
    gcd = a

print((arr[N-1] - arr[0]) // gcd + 1 - N)