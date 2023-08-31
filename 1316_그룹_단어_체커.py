def is_group_word(s):
    global ans
    appear = set()
    cur = ''
    for c in s:
        # 등장한 적이 없으면 추가
        if c not in appear: appear.add(c)
        # 등장한 적이 있는데 현재 진행중이지 않으면 실패
        elif c in appear and c != cur: return
        cur = c
    ans += 1    # return에 걸리지 않았으면 그룹 단어임


N = int(input())
ans = 0
for _ in range(N):
    is_group_word(input())
print(ans)