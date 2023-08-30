import sys; input = sys.stdin.readline

N, M, ori_B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최소 높이, 최대 높이 구하기
max_h = 0
min_h = 987654321
for i in range(N):
    for j in range(M):
        if max_h < arr[i][j]: max_h = arr[i][j]
        if min_h > arr[i][j]: min_h = arr[i][j]

# 땅의 높이를 H로 맞추려 할 때 소요되는 시간을 계산해보자
ans_time = 987654321
for H in range(min_h, max_h+1):
    B = ori_B
    time = 0
    can_do = True
    for i in range(N):
        for j in range(M):
            # H와 같은 높이인 것들은 내비둠

            # H보다 높은 것들은 내려서 인벤토리에 추가
            if arr[i][j] > H:
                time += 2 * (arr[i][j] - H)  # 블록당 2초 경과
                B += arr[i][j] - H          # 인벤토리에 추가
            
            # H보다 낮은 것들은 인벤토리에서 꺼내서 쌓음
            elif arr[i][j] < H:
                need = H - arr[i][j]    # 이만큼 필요함
                if B < need:
                    can_do = False
                    break
                else:
                    B -= need           # 인벤토리에서 꺼냄
                    time += need        # 블록당 1초 경과

        if not can_do: break
    if not can_do: continue     # 인벤토리에 블록이 부족했을 경우 다음 H 검사

    if ans_time >= time:    # 답이 여러 개 있으면
        ans_time = time
        ans_height = H      # 땅의 높이가 가장 높은 것으로 출력

print(ans_time, ans_height)