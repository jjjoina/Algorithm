from collections import deque

arr = [input() for _ in range(5)]

q = deque()
ans = set()

for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            q.append([i, j, (i, j), 0])
        else:
            q.append([i, j, {(i, j)}, 1])

while q:
    i, j, s, cnt_y = q.popleft()

    if cnt_y > 3:
        continue
    
    if len(s) == 7:
        s = tuple(s)
        ans.add(s)
        continue
    
    for di, dj in [[0, 1], [1, 0], [0, -1] ,[-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) not in s:
            s.add((ni, nj))
            if arr[ni][nj] == 'Y':
                cnt_y += 1
            q.append([ni, nj, s, cnt_y])

print(len(ans))
print(ans)