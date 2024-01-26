import sys; input = sys.stdin.readline

arr_ori = [list(map(int, input().split())) for _ in range(10)]

ret = []
# 크기가 N X N인 색종이부터 붙이기 시작했을 때 최소값
# 붙이는 게 불가능하면 append하지 않음
for N in range(5, 0, -1):
    # arr : arr_ori의 깊은 복사
    arr = [row[:] for row in arr_ori]
    cnt = [0, 5, 5, 5, 5, 5]
    # 큰 색종이부터 진행 (n x n 색종이)
    for n in range(N, 0, -1):
        for i in range(11-n):
            for j in range(11-n):
                # 각 칸으로부터 n x n이 모두 1인지 검사
                all_1 = True
                for in_i in range(n):
                    for in_j in range(n):
                        if not arr[i+in_i][j+in_j]:
                            all_1 = False
                            break
                    if not all_1:
                        break
                # 색종이를 붙일 수 있는 영역이고 색종이가 남아있다면
                if all_1 and cnt[n]:
                    cnt[n] -= 1    # 색종이 하나 사용
                    for in_i in range(n):
                        for in_j in range(n):
                            # 색종이 붙인 영역 모두 0으로 변경
                            arr[i+in_i][j+in_j] = 0

    # 1 남아있는지 확인
    exist_1 = False
    for i in range(10):
        for j in range(10):
            if arr[i][j]:
                exist_1 = True
                break
        if exist_1:
            break

    if not exist_1:
        ret.append(25 - sum(cnt))

if ret:
    print(min(ret))
else:
    print(-1)