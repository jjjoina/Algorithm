import sys; input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

checked = [False] * N
ans = 987654321

for i in range(N):
    if checked[i]:
        continue
    
    if A[i] - i * K < 1:
        continue
    
    rst = N
    for j in range(N):
        if A[j] == A[i] + (j-i) * K:
            rst -= 1
            checked[j] = True
        
    if ans > rst:
        ans = rst

print(ans)