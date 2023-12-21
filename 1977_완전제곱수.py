M = int(input())
N = int(input())

lst = []
for i in range(1, 101):
    if M <= i**2 <= N:
        lst.append(i**2)

if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)