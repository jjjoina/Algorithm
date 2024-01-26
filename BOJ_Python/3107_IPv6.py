s = input()

if '::' in s:
    lst1, lst2 = s.split('::')
    g1 = lst1.split(':')
    g2 = lst2.split(':')
    if '' in g1: g1 = []
    if '' in g2: g2 = []
    lst = []
    lst.extend(g1)
    lst.extend(['0000'] * (8-len(g1)-len(g2)))
    lst.extend(g2)
else:
    lst = s.split(':')

for i in range(8):
    while len(lst[i]) < 4:
        lst[i] = '0' + lst[i]

print(':'.join(lst))