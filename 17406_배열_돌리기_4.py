import sys; input = sys.stdin.readline
import copy

def permutation(i):
    if i == K-1:
        perm = order[:]     # 순열 생성 완료
        orders.append(perm)
        return

    for j in range(i, K):
        order[i], order[j] = order[j], order[i]
        permutation(i+1)
        order[i], order[j] = order[j], order[i]


# 배열 회전하는 함수
def rotate(operations):
    # operations : r, c, s가 담긴 배열 (연산)
    r, c, s = operations
    for i in range(1, s+1):
        cr, cc = r-1-i, c-1-i   # current row, current column
        t = temp[cr][cc]
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            for _ in range(2*i):
                temp[cr][cc] = temp[cr+dr][cc+dc] # 값 이동
                cr, cc = cr+dr, cc+dc   # curr 변경
        temp[r-1-i][c-i] = t     # 잘못된 값 제대로
        

# 배열의 행, 열, 연산의 개수
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
operations = [list(map(int, input().split())) for _ in range(K)]

# 각 순열 생성
# 0, 1, 2, ..., K-1 숫자들의 순열 생성
order = list(range(K))
orders = []
permutation(0)  # orders에 모든 순열 담음

values = []     # ans의 후보들 (배열의 값들 모음)
for o in orders:    # o : 연산 순서 (순열)
    temp = copy.deepcopy(arr)   # 따로 복사해서 연산 진행
    for i in o:     # i : K개의 연산 중 i번째 연산
        rotate(operations[i])   # 연산대로 회전
    # K번 회전 연산 완료
    # 배열의 값 계산 (sum(각 행) 중 최솟값)
    value = sum(temp[0])
    for row in temp:
        if value > sum(row):
            value = sum(row)
    values.append(value)    # 배열의 값 추가

print(min(values))