import sys; input = sys.stdin.readline
from collections import deque

def choose_M(i, prev):
    global ans

    if i == M:
        ans = min(ans, chicken_distance())
        return
    
    # i번째 치킨집으로 crs[j] 선택
    for j in range(prev+1, len(crs)-M+i+1):
        choice.append(crs[j])
        choose_M(i+1, j)
        choice.pop()


# def chicken_distance():
#     # choice가 정해진 상황에서 치킨 거리 구하기
#     cd = 0  # 치킨 거리 (chicken distance)
#     visited = [[-1] * N for _ in range(N)]
#     q = deque(choice)
#     for i, j in q:
#         visited[i][j] = 0
#     while q:
#         i, j = q.popleft()
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#                 if arr[ni][nj] == 1:        # 가정집인 경우
#                     cd += visited[ni][nj]   # 치킨 거리 누적

#     return cd


def chicken_distance():
    cd = 0
    for hi, hj in hs:           # 각 집마다
        d = 987654321
        for ci, cj in choice:   # 각 치킨집까지의 거리 중 최소값 갱신
            d = min(d, abs(hi-ci) + abs(hj-cj))
        cd += d
    return cd
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨집 좌표 구하기
hs = []     # houses
crs = []    # chicken restaurants
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hs.append((i, j))
        if arr[i][j] == 2:
            crs.append((i, j))

choice = []     # 고른 치킨집 리스트
ans = 987654321
choose_M(0, -1)
print(ans)