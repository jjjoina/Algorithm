for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[3] - lst[1] >= 4:
        print('KIN')
    else:
        print(lst[1]+lst[2]+lst[3])