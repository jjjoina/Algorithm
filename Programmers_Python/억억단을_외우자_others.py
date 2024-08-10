def solution(e, starts):
    num_of_divisor = [0] * (e + 1)

    for i in range(2, e + 1):					# i라는 약수의 관점으로 접근합니다.
        for j in range(1, min(i, e // i + 1)):	# j가 i 미만이면서 i*j가 e 이상이 되지 않도록 순회합니다.
            num_of_divisor[i * j] += 2			# i*j는 i와 j라는 약수를 가집니다.

    for i in range(1, int(e ** 0.5) + 1):
        num_of_divisor[i ** 2] += 1				# 제곱수는 제곱근이라는 약수를 하나 더 가집니다.

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