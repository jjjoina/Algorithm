import sys; input = sys.stdin.readline

def f():
    # peek = stack[-1]
    stack = []
    ret = []
    # 스택에 넣을 순서인 수
    cnt = 1
    for _ in range(int(input())):
        n = int(input())

        # [push] n이 cnt보다 같거나 큰 경우
        if n >= cnt:
            # cnt부터 n까지 push
            for i in range(cnt, n+1):
                stack.append(i)
                ret.append('+')
                cnt += 1
            stack.pop()
            ret.append('-')

        # [pop] n이 cnt보다 작은 경우.
        # pop할 때 바로 나와야 한다!!!
        # 바로 pop이 안 나오고 숫자를 날려버리면 그 숫자는 다시는 못 쓰므로.
        else:
            if stack.pop() != n:
                return ['NO']
            ret.append('-')
    return ret

for e in f():
    print(e)