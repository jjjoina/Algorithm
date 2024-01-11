import sys; input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    visited[si][sj] = 1
    q = deque()
    # 1이 아니면 퍼짐


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 리스트 만들기
zero_lst = []
len_of_zero_lst = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_lst.append([i, j])
            len_of_zero_lst += 1

# 빈칸에서 3개 조합 고르기
for first in range(len_of_zero_lst - 2):
    arr[first[0]][first[1]] = 1
    for second in range(first + 1, len_of_zero_lst - 1):
        arr[second[0]][second[1]] = 1
        for third in range(second + 1, len_of_zero_lst):
            # 해당 조합에 벽 세우기
            arr[third[0]][third[1]] = 1
            
            # 바이러스 퍼트리기
            visited = [[0] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 2 and visited[i][j] == 0:
                        bfs(i, j)

            # 빈 칸 개수 세기 -> ans

            arr[third[0]][third[1]] = 0     # 원복
        arr[second[0]][second[1]] = 0       # 원복
    arr[first[0]][first[1]] = 0             # 원복
    