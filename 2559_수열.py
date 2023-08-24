import sys; input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = [0] * (N-K+1)
sum_v[0] = sum(arr[:K])
for i in range(1, N-K+1):
    sum_v[i] = sum_v[i-1] - arr[i-1] + arr[i+K-1]

print(max(sum_v))