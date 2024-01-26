import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(arr, depth, N):
    if depth == K:
        rst[depth].extend(arr)
        return
    
    dfs(arr[:N//2], depth+1, N//2)
    rst[depth].append(arr[N//2])
    dfs(arr[N//2+1:], depth+1, N//2)


K = int(input())
lst = list(map(int, input().split()))

rst = [[] for _ in range(K+1)]
dfs(lst, 1, 2**K-1)

for i in range(1, K+1):
    print(*rst[i])