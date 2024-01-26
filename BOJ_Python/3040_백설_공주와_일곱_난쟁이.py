def solve():
    sum_v = sum(lst)
    for i in range(8):
        for j in range(i+1, 9):
            if sum_v - lst[i] - lst[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(lst[k])
                return

lst = [int(input()) for _ in range(9)]
solve()