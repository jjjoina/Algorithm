import sys; input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
gnd = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    gnd[x-1][y-1].append(z)
food = [[5] * N for _ in range(N)]

for _ in range(K):
    # <봄>
    for i in range(N):
        for j in range(N):
            # 나이가 어린 나무부터
            # (나무는 나이 기준 오름차순으로 유지됨)
            for t in range(len(gnd[i][j])):
                # 만약 양분이 부족하다면 나무는 죽는다.
                if gnd[i][j][t] > food[i][j]:
                    for k in range(t, len(gnd[i][j])):
                        food[i][j] += gnd[i][j].pop() // 2
                    break
                else:
                    # 자신의 나이만큼 양분을 먹고
                    food[i][j] -= gnd[i][j][t]
                    # 나이가 1 증가한다.
                    gnd[i][j][t] += 1

    # # <여름>
    # # 봄에 죽은 나무가 양분으로 변한다.
    # # dead_trees 역순으로 순회
    # for idx in range(len(dead_trees)-1, -1, -1):
    #     i, j, t = dead_trees[idx]
    #     # (죽은 나무의 나이 // 2)만큼 양분 증가
    #     food[i][j] += gnd[i][j][t] // 2
    #     # 죽은 나무 arr에서 pop
    #     gnd[i][j].pop()

    # <가을>
    # 나무 전체 순회
    for i in range(N):
        for j in range(N):
            for t in range(len(gnd[i][j])):
                # 나이가 5의 배수이면
                if gnd[i][j][t] % 5 == 0:
                    # 인접한 8개의 칸에
                    for di, dj in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                        ni, nj = i+di, j+dj
                        # 인덱스 체크
                        if 0 <= ni < N and 0 <= nj < N:
                            # 1살 나무 appendleft
                            gnd[ni][nj].appendleft(1)
    
    # <겨울>
    # food 순회하면서
    for i in range(N):
        for j in range(N):
            # A[i][j]만큼 증가
            food[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(gnd[i][j])
print(ans)
