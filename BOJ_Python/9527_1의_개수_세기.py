def init_dp():
    dp = [0]
    p = 1
    max_p = pow(10, 16)

    while p <= max_p:
        dp.append(dp[-1] + dp[-1] + p)
        p *= 2

    return dp


def integer_to_bit(n):
    bits = []

    while n > 0:
        bits.append(n % 2)
        n //= 2

    return bits


def compute(n):
    '''
    0 ~ n을 이진수로 표현했을 때 1의 개수의 합을 반환하는 함수
    '''
    bits = integer_to_bit(n)
    count_1 = 0
    result = 0

    for i in range(len(bits) - 1, -1, -1):
        if bits[i] == 1:
            result += dp[i] + count_1 * pow(2, i)
            count_1 += 1

    return result + count_1


A, B = map(int, input().split())

dp = init_dp()

print(compute(B) - compute(A - 1))