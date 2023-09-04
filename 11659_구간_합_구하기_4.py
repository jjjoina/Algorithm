import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
memo = [0] * (N+1)
for i in range(1, N+1):
    memo[i] = memo[i-1] + arr[i]
for _ in range(M):
    i, j = map(int, input().split())
    print(memo[j] - memo[i-1])