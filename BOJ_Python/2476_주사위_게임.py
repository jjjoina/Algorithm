import sys; input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    cnt = [0] * 7
    a, b, c = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1
    cnt[c] += 1

    if 3 in cnt:
        prize = 10000 + cnt.index(3) * 1000
    elif 2 in cnt:
        prize = 1000 + cnt.index(2) * 100
    else:
        for i in range(6, 0, -1):
            prize = i * 100
            break
    
    ans = max(ans, prize)

print(ans)