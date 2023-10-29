import sys; input = sys.stdin.readline

def perm(i, prev):
    if i == L:
        v = c = 0
        for a in s:
            if a in vowels:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print(''.join(s))
        return
    
    for j in range(prev+1, C-L+1+i):
        s.append(lst[j])
        perm(i+1, j)
        s.pop()


L, C = map(int, input().split())
lst = sorted(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
s = []
perm(0, -1)