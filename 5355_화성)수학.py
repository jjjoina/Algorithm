import sys; input = sys.stdin.readline

for _ in range(int(input())):
    lst = input().split()
    lst[0] = float(lst[0])
    
    for i in range(1, len(lst)):
        if lst[i] == '@':
            lst[0] *= 3
        elif lst[i] == '%':
            lst[0] += 5
        else:
            lst[0] -= 7

    print(f'{lst[0]:.2f}')
