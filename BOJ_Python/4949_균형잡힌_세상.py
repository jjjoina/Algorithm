import sys; input = sys.stdin.readline

s = input()
while s != '.\n':
    stack = []
    ans = 'yes'
    for c in s:
        if c in ['(', '[']:
            stack.append(c)
        elif c == ')':
            # 스택이 비어있거나 짝이 안 맞는 경우
            if not stack or stack[-1] != '(':
                ans = 'no'
                break
            else:
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                ans = 'no'
                break
            else:
                stack.pop()
    if stack:
        ans = 'no'
    print(ans)

    s = input()