T = int(input())
for t in range(1, T+1):
    ps = input()
    stack = []
    ans = 'YES'
    for b in ps:
        if b == '(':
            stack.append(b)
        else:   # b == ')'
            # 스택이 비어있으면 ans = NO
            if not stack:
                ans = 'NO'
                break
            # 스택이 비어있지 않으면 (=스택에 '('가 있으면)
            else:
                stack.pop()
    # 검사가 끝났는데도 스택에 '('가 남아있으면 ans = NO
    if stack:
        ans = 'NO'
    print(ans)