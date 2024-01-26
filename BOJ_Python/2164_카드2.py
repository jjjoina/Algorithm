import sys; input = sys.stdin.readline

def push(e):
    global rear
    rear += 1
    q.append(e)

def pop():
    global front
    front += 1
    return q[front]

N = int(input())
q = list(range(1, N+1))
front = -1
rear = -1 + N

while rear - front > 1:
    pop()
    push(pop())

print(q[rear])