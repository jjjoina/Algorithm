import sys; input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(input().strip())

ans = 0
visited = [0] * N

for i in range(N):
    if lst[i] == 'P':
        for d in range(-K, K+1):
            if 0 <= i+d < N:
                if lst[i+d] == 'H' and not visited[i+d]:
                    visited[i+d] = 1
                    ans += 1
                    break

print(ans)