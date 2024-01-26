lst = [[int(input()), i] for i in range(8)]
lst.sort(reverse=True)

idx_lst = [0] * 8
sum_v = 0
for val, idx in lst[:5]:
    sum_v += val
    idx_lst[idx] = 1

print(sum_v)

for i in range(8):
    if idx_lst[i]:
        print(i+1, end=' ')