rows = []
cols = []
for _ in range(3):
    r, c = map(int, input().split())
    if r not in rows:
        rows.append(r)
    else:
        rows.remove(r)
    if c not in cols:
        cols.append(c)
    else:
        cols.remove(c)
print(rows[0], cols[0])