# 풀이 1. [452ms] Brute Force

N = int(input())

MAX = N

set1 = set()
set2 = set()
set3 = set()

for i in range(int(MAX**0.5) + 1):
    set1.add(i**2)
list1 = sorted(set1)
l = len(list1)

for i in range(l):
    if list1[i] * 2 > MAX:
        break
    for j in range(i, l):
        n = list1[i] + list1[j]
        if n > MAX:
            break
        if n not in set1:
            set2.add(n)

for i in range(l):
    if list1[i] * 3 > MAX:
        break
    for j in range(i, l):
        if list1[i] + list1[j] * 2 > MAX:
            break
        for k in range(j, l):
            n = list1[i] + list1[j] + list1[k]
            if n > MAX:
                break
            if n not in set1 and n not in set2:
                set3.add(n)

if N in set1:
    print(1)
elif N in set2:
    print(2)
elif N in set3:
    print(3)
else:
    print(4)