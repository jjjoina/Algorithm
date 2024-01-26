lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for ca in lst:
    s = s.replace(ca, '1')
print(len(s))