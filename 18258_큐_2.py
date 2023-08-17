# # 풀이 3. [정답] front, rear
# import sys; input = sys.stdin.readline

# q = [0] * 2_000_000
# front = rear = -1

# N = int(input())
# for _ in range(N):
#     # c : 명령어 (command)
#     c = input().strip()
#     if c[:4] == 'push':
#         rear += 1
#         q[rear] = c[5:]
    
#     elif c == 'pop':
#         if front < rear:
#             front += 1
#             print(q[front])
#         else: print(-1)

#     elif c == 'size':
#         print(rear - front)

#     elif c == 'empty':
#         if front == rear: print(1)
#         else: print(0)

#     elif c == 'front':
#         if front < rear: print(q[front+1])
#         else: print(-1)

#     elif c == 'back':
#         if front < rear: print(q[rear])
#         else: print(-1)


# # 풀이 2. [정답] deque
# import sys; input = sys.stdin.readline

# from collections import deque
# q = deque()

# N = int(input())
# for _ in range(N):
#     # c : 명령어 (command)
#     c = input().strip()
#     if c[:4] == 'push':
#         q.append(c[5:])
    
#     elif c == 'pop':
#         if q: print(q.popleft())
#         else: print(-1)

#     elif c == 'size':
#         print(len(q))

#     elif c == 'empty':
#         if q: print(0)
#         else: print(1)

#     elif c == 'front':
#         if q: print(q[0])
#         else: print(-1)

#     elif c == 'back':
#         if q: print(q[-1])
#         else: print(-1)


# # 풀이 1. [시간 초과] append, pop(0)
# import sys; input = sys.stdin.readline

# q = []

# N = int(input())
# for _ in range(N):
#     # c : 명령어 (command)
#     c = input().strip()
#     if c[:4] == 'push':
#         q.append(c[5:])

#     elif c == 'pop':
#         if q: print(q.pop(0))
#         else: print(-1)

#     elif c == 'size':
#         print(len(q))

#     elif c == 'empty':
#         if q: print(0)
#         else: print(1)

#     elif c == 'front':
#         if q: print(q[0])
#         else: print(-1)

#     elif c == 'back':
#         if q: print(q[-1])
#         else: print(-1)