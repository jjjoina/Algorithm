# 풀이 2. [정답] 스택 활용
import sys; input = sys.stdin.readline
stack1 = list(input().strip())  # 커서를 기준으로 왼쪽에 있는 문자열들의 스택
stack2 = []     # 커서를 기준으로 오른쪽에 있는 문자들의 스택. 실제 문자열의 역순으로 쌓인다!!!
M = int(input())

for _ in range(M):
    c = input().split()
    if c[0] == 'L':
        if stack1: stack2.append(stack1.pop())
    elif c[0] == 'D':
        if stack2: stack1.append(stack2.pop())
    elif c[0] == 'B':
        if stack1: stack1.pop()
    elif c[0] == 'P':
        stack1.append(c[1])

print(''.join(stack1) + ''.join(stack2[::-1]))



# 풀이 1. [시간 초과]
# import sys; input = sys.stdin.readline

# s = [''] + list(input().strip())
# cursor = len(s) - 1
# M = int(input())
# for _ in range(M):
#     c = input().split()
#     if c[0] == 'L' and cursor > 0:
#         cursor -= 1
#     elif c[0] == 'D' and cursor < len(s)-1:
#         cursor += 1
#     elif c[0] == 'B' and cursor > 0:
#         s.pop(cursor)
#         cursor -= 1
#     elif c[0] == 'P':
#         cursor += 1
#         s.insert(cursor, c[1])
# print(''.join(s))
