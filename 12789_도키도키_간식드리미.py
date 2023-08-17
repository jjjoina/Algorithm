import sys; input = sys.stdin.readline

def snack():
    now = 1
    stack = []
    for n in arr:
        while stack and stack[-1] == now:
            res.append(stack.pop())
            now += 1
        if n == now:
            res.append(n)
            now += 1
        else:
            stack.append(n)

    # 스택에 남아있는 사람 pop
    while stack:
        if stack[-1] == now:
            res.append(stack.pop())
            now += 1
        else:
            return 'Sad'

    return 'Nice'


N = int(input())
arr = list(map(int, input().split()))
res = []
print(snack())