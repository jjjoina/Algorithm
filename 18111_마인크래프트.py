import sys; input = sys.stdin.readline

N, M, ori_B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최소 높이, 최대 높이, 높이의 합 구하기
max_h = 0
min_h = 987654321
sum_h = 0
for i in range(N):
    for j in range(M):
        if max_h < arr[i][j]: max_h = arr[i][j]
        if min_h > arr[i][j]: min_h = arr[i][j]
        sum_h += arr[i][j]

# 땅의 높이를 H로 맞추려 할 때 소요되는 시간을 계산해보자
ans_time = 987654321
for H in range(min_h, max_h+1):
    B = ori_B
    time = 0

    # 불가능한 경우 먼저 쳐내기
    if sum_h + B < N*M*H: continue

    for i in range(N):
        for j in range(M):
            # 1. 높은 높이에서 블럭 빼와서 인벤토리에 추가하기
            if arr[i][j] > H:
                time += 2 * (arr[i][j] - H)
            # 2. 인벤토리에 있는 블럭들로 낮은 높이 채우기
            else:
                time += H - arr[i][j]

    # time : 걸린 시간
    if ans_time >= time:
        ans_time = time
        ans_height = H      # 최소 시간이 여러 개면 가장 높은 것이 정답

print(ans_time, ans_height)