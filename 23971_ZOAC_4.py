# H행 W열
H, W, N, M = map(int, input().split())
A = H / (N+1)
B = W / (M+1)
if A > int(A): A = int(A) + 1
if B > int(B): B = int(B) + 1
print(int(A*B))