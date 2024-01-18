import sys; input = sys.stdin.readline

user_set = set()
ans = 0

for _ in range(int(input())):
    s = input().strip()
    
    if s == 'ENTER':
        user_set.clear()
    else:
        if s not in user_set:
            user_set.add(s)
            ans += 1

print(ans)