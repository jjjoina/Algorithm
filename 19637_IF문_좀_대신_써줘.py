import sys; input = sys.stdin.readline

N, M = map(int, input().split())
rst = [''] * 1000000001
cur = 0
for _ in range(N):
    style, value = input().split()
    value = int(value)
    
    while cur <= value:
        rst[cur] = style
        cur += 1
        
for _ in range(M):
    print(rst[int(input())])