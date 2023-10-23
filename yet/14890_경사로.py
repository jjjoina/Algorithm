import sys; input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 2 * N

# 행 탐색
for r in range(N):
    # r번째 행
    runway = [0] * N    # 경사로가 놓여진 곳 체크
    for j in range(N-1):
        # 이번 칸과 다음 칸 검사
        # 높이 차가 1보다 큰 경우 탈락
        if abs(arr[r][j] - arr[r][j+1]) > 1:
            ans -= 1
            break   # 다음 행 검사
        
        # 오르막길인 경우
        elif arr[r][j] < arr[r][j+1]:
            # 인덱스 체크
            if j-L+1 < 0:
                ans -= 1
                break   # 다음 행 검사
            # 해당 인덱스의 높이가 모두 같은가?
            possible = True
            for k in range(j-L+1, j+1):
                # 높이가 다르거나 이미 경사로가 깔려있는 경우
                if arr[r][k] != arr[r][j] or runway[k] == 1:
                    possible = False
                    break
            if possible:
                # 경사로 설치
                runway[j-L+1:j+1] = [1] * L
            else:
                ans -= 1
                break   # 다음 행 검사
            
        # 내리막길인 경우
        elif arr[r][j] > arr[r][j+1]:
            # 인덱스 체크
            if j+L >= N:
                ans -= 1
                break   # 다음 행 검사
            # 해당 인덱스의 높이가 모두 같은가?
            possible = True
            for k in range(j+1, j+1+L):
                # 높이가 다르거나 이미 경사로가 깔려있는 경우
                if arr[r][k] != arr[r][j] or runway[k] == 1:
                    possible = False
                    break
            if possible:
                # 경사로 설치
                runway[j+1:j+1+L] = [1] * L
            else:
                ans -= 1
                break   # 다음 행 검사

# 열 탐색
