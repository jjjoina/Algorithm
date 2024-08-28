def calculate(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    else:
        return operand1 * operand2


def calculate_exp(i, operand1):
    if i == N:
        global ans
        if ans < operand1:
            ans = operand1
        return

    if i + 2 < N and chosen[i + 2]:
        operand2 = calculate(exp[i + 1], exp[i + 2], exp[i + 3])
        val = calculate(operand1, exp[i], operand2)
        calculate_exp(i + 4, val)
    else:
        val = calculate(operand1, exp[i], exp[i + 1])
        calculate_exp(i + 2, val)


def choose(i):
    if i >= N:
        calculate_exp(1, exp[0])
        return

    choose(i + 2)

    chosen[i] = True
    choose(i + 4)
    chosen[i] = False


N = int(input())
exp = list(input())

for i in range(0, N, 2):
    exp[i] = int(exp[i])

chosen = [False] * N
ans = -pow(2, 31)

choose(1)

print(ans)