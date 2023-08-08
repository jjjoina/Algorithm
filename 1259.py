# str으로 받자
ans = []
while True:
    n = input()
    if n == '0':
        break
    is_p = 'yes'
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            is_p = 'no'
            break
    ans.append(is_p)

for a in ans:
    print(a)