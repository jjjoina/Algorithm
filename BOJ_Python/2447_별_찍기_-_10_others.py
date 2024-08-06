def star(n):
    if n == 1:
        return ['*']
    
    prev_rst = star(n // 3)
    rst = []

    for l in prev_rst:
        rst.append(l * 3)
    
    for l in prev_rst:
        rst.append(l + ' ' * (n // 3) + l)

    for l in prev_rst:
        rst.append(l * 3)

    return rst


N = int(input())

for row in star(N):
    print(row)