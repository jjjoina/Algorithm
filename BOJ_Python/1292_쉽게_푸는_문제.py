i = 1
cnt = 1
lst = [0]

while i < 1000:
    lst.extend([cnt]*cnt)
    i += cnt
    cnt += 1

A, B = map(int, input().split())

print(sum(lst[A:B+1]))