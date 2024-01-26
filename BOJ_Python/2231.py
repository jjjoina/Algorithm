N = int(input())
# 생성자 없으면 0
ctor = 0
# M이 생성자인지 검사
for M in range(1, N):
    # i와 i의 각 자리수의 합 구하기
    num = M
    sum_v = num
    while num > 0:
        sum_v += num % 10
        num //= 10
    if sum_v == N:
        ctor = M
        break
print(ctor)