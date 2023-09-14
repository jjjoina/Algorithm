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
