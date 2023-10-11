import sys; input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))   # 내구도

dq = deque()
for d in lst:
    dq.append([d, 0])       # [내구도, 로봇 유무]

ans = 0
zeros = lst.count(0)
while True:
    ans += 1

    dq.appendleft(dq.pop())     # 벨트 회전
    dq[N-1][1] = 0              # 내리는 위치에서 로봇 내림

    for i in range(N-2, 0, -1):
        if dq[i][1] == 1:      # 가장 먼저 올라간 로봇부터
            # 이동할 수 있다면
            # (= 다음 칸에 로봇 없음 and 다음 칸 내구도가 1 이상)
            if dq[i+1][1] == 0 and dq[i+1][0] >= 1:
                dq[i+1][1] = 1     # 이동
                dq[i][1] = 0
                dq[i+1][0] -= 1    # 내구도 감소
                if dq[i+1][0] == 0:
                    zeros += 1

                if i == N-2:
                    dq[i+1][1] = 0  # 내리는 위치 직전 칸이었으면 로봇 내림
    
    if dq[0][0] != 0:      # 올리는 위치에서 올릴 수 있으면
        dq[0][1] = 1       # 로봇 올림
        dq[0][0] -= 1      # 내구도 감소
        if dq[0][0] == 0:
            zeros += 1

    if zeros >= K:
        break

print(ans)