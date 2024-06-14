import sys; input = sys.stdin.readline

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

max_x = 0
for g, x in lst:
    if max_x < x:
        max_x = x

buckets = [0] * (max_x+1)
for g, x in lst:
    buckets[x] = g
    
ans = rst = sum(buckets[:2*K+1])
for i in range(K+1, max_x-K+1):
    rst -= buckets[i-K-1]
    rst += buckets[i+K]
    if ans < rst:
        ans = rst

print(ans)