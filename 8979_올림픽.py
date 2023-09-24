import sys; input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for c in arr:
    if c[0] == K:
        standard = c

ans = 1
for c in arr:
    if c[1] > standard[1]: ans += 1
    elif c[1] == standard[1]:
        if c[2] > standard[2]: ans += 1
        elif c[2] == standard[2]:
            if c[3] > standard[3]: ans += 1

print(ans)