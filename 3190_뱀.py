import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]   # 보드
cd_dic = {}     # change direction dictionary

for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1   # 사과

L = int(input())
for _ in range(L):
    X, C = input().split()
    X = int(X)
    C = 1 if C == 'D' else -1
    cd_dic[X] = C

arr[0][0] = 9   # 초기 뱀 표시
dir_lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0   # 처음 방향 : 우
ans = 0
snake = deque([[0, 0]]) # 뱀. 머리 ------> 꼬리

while True:
    ans += 1

    ni = snake[0][0] + dir_lst[d][0]    # 다음칸 좌표
    nj = snake[0][1] + dir_lst[d][1]

    if ni == -1 or ni == N or nj == -1 or nj == N:  # 벽과 부딪히는 경우
        break
    if arr[ni][nj] == 9:    # 자기자신과 부딪히는 경우
        break

    if arr[ni][nj] == 0:    # 이동한 칸에 사과가 없는 경우
        ti, tj = snake.pop()    # 꼬리 좌표
        arr[ti][tj] = 0
    
    arr[ni][nj] = 9     # 보드에 뱀 머리 표시
    snake.appendleft([ni, nj])

    if ans in cd_dic:
        d = (d + cd_dic[ans]) % 4

print(ans)