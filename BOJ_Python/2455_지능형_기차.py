ans = 0
cur = 0

for _ in range(4):
    down, up = map(int, input().split())
    
    cur += up - down
    
    if ans <= cur:
        ans = cur

print(ans)