import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 터진 풍선 리스트
ans = []
# 탐색용 인덱스
i = 0

while True:
    ans.append(i+1)

    # 모두 풍선이 터지면 종료
    if len(ans) == N:
        break

    # step 저장
    step = arr[i]

    # 터진 풍선 표시
    arr[i] = 0

    cnt = 0
    # step만큼 i 이동 (터진 풍선 제외)
    if step > 0:
        while cnt < step:
            i = (i+1) % N
            # 안 터진 풍선만 cnt 증가
            if arr[i]: cnt += 1
    elif step < 0:
        while cnt > step:
            i = (i-1) % N
            # 안 터진 풍선만 cnt 감소
            if arr[i]: cnt -= 1

print(*ans)