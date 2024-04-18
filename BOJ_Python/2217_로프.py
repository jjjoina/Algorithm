import sys; input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort(reverse=True)

ans = 0
for i in range(N):
    w = lst[i] * (i+1)
    if ans < w:
        ans = w
        
print(ans)