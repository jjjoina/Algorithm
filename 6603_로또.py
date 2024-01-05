import sys; input = sys.stdin.readlineZ

def comb(i, start):
    if i == 6:
        print(*c)
        return
    
    for j in range(start, lst[0]-4+i):
        c.append(lst[j])
        comb(i+1, j+1)
        c.pop()


while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break

    c = []
    comb(0, 1)
    
    print()