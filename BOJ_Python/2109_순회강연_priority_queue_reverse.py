import sys; input = sys.stdin.readline
import heapq

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]

max_d = max(d for p, d in lectures) if N else 0
schedule = [[] for _ in range(max_d+1)]
for p, d in lectures:
    schedule[d].append(p)
surplus = []
ans = 0

for d in range(max_d, 0, -1):   # d 역방향
    for p in schedule[d]:
        heapq.heappush(surplus, -p)

    if surplus:
        ans += -heapq.heappop(surplus)

print(ans)