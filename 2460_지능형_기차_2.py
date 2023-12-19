import sys; input = sys.stdin.readline

ans = 0
cur = 0
for _ in range(10):
    down, up = map(int, input().split())
    
    cur -= down
    cur += up
    
    if ans < cur:
        ans = cur
    
print(ans)