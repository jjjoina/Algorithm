import sys; input = sys.stdin.readline

def eat_row(r):
    rst = cnt = 1
    for c in range(1, N):
        if arr[r][c-1] == arr[r][c]:
            cnt += 1
            rst = max(rst, cnt)
        else:
            cnt = 1
    return rst


def eat_col(c):
    rst = cnt = 1
    for r in range(1, N):
        if arr[r-1][c] == arr[r][c]:
            cnt += 1
            rst = max(rst, cnt)
        else:
            cnt = 1
    return rst


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

# 현재 상태에서 최대 개수 구해놓기
ans = 0
for n in range(N):
    ans = max(ans, eat_row(n), eat_col(n))

for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j < N-1:     # 마지막 열은 제외
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]     # 교환
            ans = max(ans, eat_row(i), eat_col(j), eat_col(j+1))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]     # 원복

        # 아래와 교환
        if i < N-1:     # 마지막 행은 제외
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]     # 교환
            ans = max(ans, eat_col(j), eat_row(i), eat_row(i+1))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]     # 원복

print(ans)