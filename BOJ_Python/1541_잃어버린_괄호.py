# 1. split('-')
# 2. split('+')

s = input().split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
ans = 0

# 첫 번째 뭉탱이는 모두 더하기
for n in s[0]:
    ans += int(n)

# 두 번째 뭉탱이부터는 모두 더해서 ans에서 빼기
for i in range(1, len(s)):
    tmp = 0
    for j in range(len(s[i])):
        tmp += int(s[i][j])
    ans -= tmp

print(ans)