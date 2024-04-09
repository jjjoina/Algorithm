import sys; input = sys.stdin.readline
from collections import deque

def find_start_point_and_numbering_dirty():
    dirty_dict = {}
    cnt_d = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                si, sj = i, j
            elif arr[i][j] == '*':
                dirty_dict[(i, j)] = cnt_d
                cnt_d += 1
        
    return si, sj, dirty_dict, cnt_d


def clean():
    q = deque()
    visited = [[[-1] * (1<<(cnt_d)) for _ in range(w)] for _ in range(h)]
    q.append([si, sj, 0])
    visited[si][sj][0] = 0
    
    while q:
        i, j, d_bit = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] != 'x' and visited[ni][nj][d_bit] == -1:
                # 청소하지 않은 곳인 경우 -> 청소하고 enqueue
                if arr[ni][nj] == '*' and not d_bit & (1<<dirty_dict[(ni, nj)]):
                    d_idx = dirty_dict[(ni, nj)]
                    new_d_bit = d_bit | (1<<d_idx)                    
                    q.append([ni, nj, new_d_bit])
                    visited[ni][nj][new_d_bit] = visited[i][j][d_bit] + 1
                    
                    if new_d_bit == (1<<(cnt_d)) - 1:
                        return visited[ni][nj][new_d_bit]
                
                # 깨끗한 경우 -> 바로 enqueue
                else:
                    q.append([ni, nj, d_bit])
                    visited[ni][nj][d_bit] = visited[i][j][d_bit] + 1
        
    return -1


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0: break
    
    arr = [list(input().strip()) for _ in range(h)]
    
    si, sj, dirty_dict, cnt_d = find_start_point_and_numbering_dirty()
    # print(si, sj, dirty_dict, cnt_d)
    
    print(clean())