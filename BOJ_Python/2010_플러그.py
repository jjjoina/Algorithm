import sys; input = sys.stdin.readline

N = int(input())

ans = 0
for _ in range(N):
    ans += int(input())

ans -= N-1

print(ans)