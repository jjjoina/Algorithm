def solution(e, starts):
    num_of_divisor = [1] * (e + 1)  # 모든 수는 최소 1개의 약수를 가지므로 1로 초기화합니다.

    # 약수의 개수 구하는 로직
    for d in range(2, e + 1):				# d라는 약수의 관점으로 접근합니다.
        for mul in range(d, e + 1, d):		# d에서 e까지의 숫자 중 d의 배수는
            num_of_divisor[mul] += 1		# d라는 약수를 가집니다.

    rst = [0] * (e + 1)
    max_idx = e

    for i in range(e, min(starts) - 1, -1):
        if num_of_divisor[i] >= num_of_divisor[max_idx]:
            max_idx = i
        rst[i] = max_idx

    answer = []

    for s in starts:
        answer.append(rst[s])

    return answer