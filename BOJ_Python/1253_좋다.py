import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

s = set()
for i in range(N-1):
    if lst[i] != 0:
        for j in range(i+1, N):
            if lst[j] != 0:
                # 0과 더하는 경우는 배제한다.
                s.add(lst[i] + lst[j])

# 0이 있는 테스트케이스
if 0 in lst:
    cnt_d = {}
    for i in range(N):
        cnt_d[lst[i]] = cnt_d.get(lst[i], 0) + 1
    for val, cnt in cnt_d.items():
        if val == 0:
            if cnt >= 3:
                s.add(val)
        else:
            if cnt >= 2:
                s.add(val)

ans = 0
for i in range(N):
    if lst[i] in s:
        ans += 1

print(ans)