# 풀이 2. [31120KB] [232ms] DFS, 중복 감소
import sys; input = sys.stdin.readline

def dfs(lst, cnt_y):
    if cnt_y > 3:
        return
    
    if len(lst) == 7:
        ans.add(tuple(sorted(lst)))
        return
    
    for i, j in lst:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 'Y':
                    dfs(lst+[(ni, nj)], cnt_y+1)
                else:
                    dfs(lst+[(ni, nj)], cnt_y)
                visited[ni][nj] = 0


arr = [input().strip() for _ in range(5)]

visited = [[0] * 5 for _ in range(5)]
ans = set()

for i in range(5):
    for j in range(5):
        visited[i][j] = 1
        if arr[i][j] == 'Y':
            dfs([(i, j)], 1)
        else:
            dfs([(i, j)], 0)

print(len(ans))



# # 풀이 1. [337448KB] [3428ms] BFS
# import sys; input = sys.stdin.readline
# from collections import deque

# arr = [input().strip() for _ in range(5)]

# q = deque()
# ans = set()

# for idx in range(25):
#     i = idx // 5
#     j = idx % 5
#     if arr[i][j] == 'Y':
#         q.append([i, j, [idx], 1])
#     else:
#         q.append([i, j, [idx], 0])

# while q:
#     i, j, lst, cnt_y = q.popleft()

#     if cnt_y > 3:
#         continue
    
#     if len(lst) == 7:
#         lst.sort()
#         ans.add(tuple(lst))
#         continue
    
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < 5 and 0 <= nj < 5 and ni * 5 + nj not in lst:
#             n_lst = lst + [ni * 5 + nj]
#             n_cnt_y = cnt_y + 1 if arr[ni][nj] == 'Y' else cnt_y
#             for idx in lst:
#                 q.append([idx//5, idx%5, n_lst[:], n_cnt_y])

# print(len(ans))