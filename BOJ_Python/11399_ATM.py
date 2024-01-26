N = int(input())
arr = list(map(int, input().split()))
arr.sort()
memo = [0] * N
memo[0] = arr[0]
for i in range(1, N):
    memo[i] = memo[i-1] + arr[i]
print(sum(memo))