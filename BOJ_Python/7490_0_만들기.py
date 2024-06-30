def calculate(exp):
    rst = 0
    operand = 0
    operator = 1
    
    for c in exp:
        if c == ' ':
            operand *= 10
        elif c == '+' or c == '-':
            rst += operator * operand
            operator = 1 if c == '+' else -1
            operand = 0
        else:
            operand += int(c)
    rst += operator * operand
    
    return rst


def dfs(exp, depth):
    if depth == N:
        if calculate(exp) == 0:
            print(exp)
        return
    
    dfs(exp + ' ' + str(depth+1), depth+1)
    dfs(exp + '+' + str(depth+1), depth+1)
    dfs(exp + '-' + str(depth+1), depth+1)


for _ in range(int(input())):
    N = int(input())
    dfs('1', 1)
    print()