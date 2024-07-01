import math

def count(m):
    cnt = 0
    for i in range(1, m):
        if m ** 2 > i * N:
            cnt += 1 + (N-i) * 2
        else:
            cnt += 1 + (math.ceil(m**2/i) - i - 1) * 2
    return cnt


N = int(input())
k = int(input())

# for i in range(1, N+2):
#     print(f'count({i}) = {count(i)}')

s, e = 1, N+1
while s <= e:
    m = (s + e) // 2
    if count(m) < k:
        s = m + 1
    else:
        e = m - 1
        
# print(e)
        
lst = []
for i in range(1, e+1):
    n = i * math.ceil(e**2 / i)
    while n < (e+1) ** 2 and n <= i * N:
        lst.append(n)
        lst.append(n)  
        n += i
# print(lst)
lst.sort()

print(lst[k-count(e)])