import sys; input = sys.stdin.readline

K = int(input())

for i in range(1, K+1):
    lst = list(map(int, input().split()))
    N, *lst = lst
    lst.sort(reverse=True)
    max_gap = 0
    for j in range(N-1):
        gap = lst[j] - lst[j+1]
        if max_gap < gap:
            max_gap = gap

    print(f'Class {i}')
    print(f'Max {max(lst)}, Min {min(lst)}, Largest gap {max_gap}')