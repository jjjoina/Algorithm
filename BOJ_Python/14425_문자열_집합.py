import sys; input = sys.stdin.readline

N, M = map(int, input().split())
s = set()
for _ in range(N):
    s.add(input())

ans = 0
for _ in range(M):
    if input() in s: ans += 1
print(ans)