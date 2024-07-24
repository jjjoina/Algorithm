import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

fruit_cnt = [0] * 10
fruit_cnt[lst[0]] = 1
cnt = 1
l = r = 0
ans = 0

while True:
    if cnt <= 2:
        ans = max(ans, r-l+1)
        r += 1
        if r == N:
            break
        fruit_cnt[lst[r]] += 1
        if fruit_cnt[lst[r]] == 1:
            cnt += 1

    else:
        l += 1
        fruit_cnt[lst[l-1]] -= 1
        if fruit_cnt[lst[l-1]] == 0:
            cnt -= 1

print(ans)