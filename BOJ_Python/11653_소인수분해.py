N = int(input())
for i in range(2, N+1):
    # i가 N의 약수이면
    # (이때 i는 소수일 때만 걸릴수밖에 없음)
    # why? i가 합성수이면 이전에 i의 약수에서 모두 빼냈으므로
    while N % i == 0:
        print(i)
        N //= i