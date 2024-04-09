import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

l, r = 0, N-1
ans = [lst[l], lst[r]]

while l < r:
    if abs(lst[l] + lst[r]) <= abs(sum(ans)):
        ans = [lst[l], lst[r]]
        
    if lst[l] + lst[r] == 0:
        break
    elif lst[l] + lst[r] < 0:
        l += 1
    else:
        r -= 1
        
print(*ans)