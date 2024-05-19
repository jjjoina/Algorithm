ans = []

for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        ans.append(i)

if ans:
    print(*ans)
else:
    print('HE GOT AWAY!')