import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

cs = [0] * N    # 누적합

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i] and cs[i] < cs[j]:
            cs[i] = cs[j]
    cs[i] += lst[i]
    
print(max(cs))