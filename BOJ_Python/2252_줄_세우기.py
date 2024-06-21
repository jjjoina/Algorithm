import sys; input = sys.stdin.readline

N, M = map(int, input().split())
in_degrees = [0] * (N+1)
outs = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    in_degrees[B] += 1
    outs[A].append(B)

q = []
for i in range(1, N+1):
    if in_degrees[i] == 0:
        q.append(i)
        
ans = []
while q:
    v = q.pop()
    ans.append(v)
    for w in outs[v]:
        in_degrees[w] -= 1
        if in_degrees[w] == 0:
            q.append(w)
            
print(*ans)