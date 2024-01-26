# 6이 3개 이상 연속으로 들어가는 수
# 1부터 증가하면서 6이 연속으로 3개 이상 들어가지 않는 수는 제외
# 6이 연속으로 3개 이상 들어가는 수가 나오면 cnt += 1

N = int(input())
ans = 665   # 우선 처음엔 첫 번째 종말의 수로 설정
cnt = 0
while cnt < N:
    ans += 1
    s = str(ans)
    if '666' in s:
        cnt += 1
print(ans)