import sys; input = sys.stdin.readline

S = input().strip()

cnt = [0] * 2
cur = ''

for c in S:
    if c == cur:
        continue

    cur = c
    cnt[int(c)] += 1

print(min(cnt))