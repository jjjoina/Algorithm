import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

sum_ = sum(lst)
bbh = 2 * (sum_ - lst[0] - lst[1])          # 벌-벌-통
hbb = (sum_ - lst[N-1] - lst[1]) + lst[0]   # 통-벌-벌
bhb = (sum_ - lst[0] - lst[N-1]) + lst[1]   # 벌-통-벌
ans = max(bbh, hbb, bhb)

for i in range(2, N-1):
    bbh += lst[i-1] - 2 * lst[i]
    hbb += 2 * lst[i-1] - lst[i]
    bhb += lst[i] - lst[i-1]
    ans = max(ans, bbh, hbb, bhb)

print(ans)