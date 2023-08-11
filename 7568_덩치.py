# 몸무게, 키가 둘 다 커야만 덩치 큼
# 둘 중 하나만 크면 판별 불가
# 자신보다 덩치가 큰 사람이 k명이면 등수는 k+1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = []
for person in arr:
    cnt = 1
    for compare in arr:
        if person[0] < compare[0] and person[1] < compare[1]:
            cnt += 1
    ans.append(cnt)
print(*ans)