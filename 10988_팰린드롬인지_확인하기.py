s = input()
ans = 1
for i in range(len(s)//2+1):
    if s[i] != s[len(s)-1-i]: ans = 0
print(ans)