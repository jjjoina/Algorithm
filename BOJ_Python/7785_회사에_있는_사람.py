import sys; input = sys.stdin.readline

n = int(input())
company = set()
for _ in range(n):
    log = input().split()
    if log[1] == 'enter':
        company.add(log[0])
    else:
        company.remove(log[0])
rst = list(company)
rst.sort(reverse=True)
for s in rst:
    print(s)