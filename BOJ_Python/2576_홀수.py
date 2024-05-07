sum_v = 0
min_v = 987654321

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        sum_v += n
        if min_v > n:
            min_v = n
        
if sum_v == 0:
    print(-1)
else:
    print(sum_v)
    print(min_v)