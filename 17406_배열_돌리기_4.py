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
# def rotate()


# 과 동시에 배열 회전
# 과 동시에 배열의 값 계산
# 과 동시에 ans 최솟값으로 갱신

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
for o in orders:    # 순열 별로
    for i in o:     # i : K개 중 i번째 연산
        rotate(operations[i])   # 연산대로 회전
    # K번 회전 연산 완료
    # 배열의 값 계산
    value = 0
    for row in arr:
    

    
    # 배열 복사한 다음에 연산 진행해야 할 듯 ....



    values.append(value)    # 배열의 값 추가