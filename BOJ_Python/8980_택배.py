import sys; input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]

arr.sort(key=lambda x: x[1])   # to 순으로 정렬

truck = [0] * (N+1)
ans = 0

for f, t, c in arr:
    load = min(c, C - max(truck[f:t]))

    if load == 0: continue

    for t_idx in range(f, t):
        truck[t_idx] += load
    
    ans += load

print(ans)