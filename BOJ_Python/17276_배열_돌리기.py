import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 시계 방향으로만 회전
    d %= 360
    # 회전 횟수
    d //= 45

    # d번 회전
    for _ in range(d):
        # 부대각선(우상향)만 따로 임시로 저장
        ori_sa = []
        for i in range(n):
            ori_sa.append(arr[n-1-i][i])
        # 회전 1회
        for i in range(n):
            arr[n//2][i], arr[i][i], arr[i][n//2], arr[i][n-1-i]\
                = ori_sa[i], arr[n//2][i], arr[i][i], arr[i][n//2]
            
    for row in arr:
        print(*row)