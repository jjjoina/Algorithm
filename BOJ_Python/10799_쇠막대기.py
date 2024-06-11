import sys; input = sys.stdin.readline

lst = list(input().strip())

cnt = 0
ans = 0

i = 0
len_lst = len(lst)
while i < len_lst:
    if lst[i] == '(':
        if lst[i+1] == ')':
            ans += cnt
            i += 2
        else:
            cnt += 1
            i += 1
    else:
        cnt -= 1
        ans += 1
        i += 1
        
print(ans)