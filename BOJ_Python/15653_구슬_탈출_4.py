import sys; input = sys.stdin.readline
from collections import deque

def find_start_points():
    for r in range(1, N-1):
        for c in range(1, M-1):
            if arr[r][c] == 'B':
                sbr, sbc = r, c
            elif arr[r][c] == 'R':
                srr, src = r, c
    
    return sbr, sbc, srr, src


def tilt(br, bc, rr, rc):
    rst_lst = []
    
    # 왼쪽으로 기울이기
    nbr, nbc, nrr, nrc = br, bc, rr, rc
    fall_together = False
    
    while arr[nbr][nbc-1] != '#' and arr[nbr][nbc] != 'O':
        nbc -= 1
    while arr[nrr][nrc-1] != '#' and arr[nrr][nrc] != 'O':
        nrc -= 1
    
    if nbr == nrr and nbc == nrc:   # 굴렸는데 같은 곳에 도착한 경우
        if arr[nbr][nbc] == 'O':    # 같이 구멍에 빠지는 경우
            fall_together = True
        elif bc < rc:
            nrc += 1
        else:
            nbc += 1
    
    if (nbr, nbc, nrr, nrc) not in visited_dic and arr[nbr][nbc] != 'O' and not fall_together:
        visited_dic[(nbr, nbc, nrr, nrc)] = visited_dic[(br, bc, rr, rc)] + 1
        rst_lst.append((nbr, nbc, nrr, nrc))
    
    # 오른쪽으로 기울이기
    nbr, nbc, nrr, nrc = br, bc, rr, rc
    fall_together = False

    while arr[nbr][nbc+1] != '#' and arr[nbr][nbc] != 'O':
        nbc += 1
    while arr[nrr][nrc+1] != '#' and arr[nrr][nrc] != 'O':
        nrc += 1
    
    if nbr == nrr and nbc == nrc:   # 굴렸는데 같은 곳에 도착한 경우
        if arr[nbr][nbc] == 'O':    # 같이 구멍에 빠지는 경우
            fall_together = True
        if bc < rc:
            nbc -= 1
        else:
            nrc -= 1
    
    if (nbr, nbc, nrr, nrc) not in visited_dic and arr[nbr][nbc] != 'O' and not fall_together:
        visited_dic[(nbr, nbc, nrr, nrc)] = visited_dic[(br, bc, rr, rc)] + 1
        rst_lst.append((nbr, nbc, nrr, nrc))
    
    # 위쪽으로 기울이기
    nbr, nbc, nrr, nrc = br, bc, rr, rc
    fall_together = False

    while arr[nbr-1][nbc] != '#' and arr[nbr][nbc] != 'O':
        nbr -= 1
    while arr[nrr-1][nrc] != '#' and arr[nrr][nrc] != 'O':
        nrr -= 1
    
    if nbr == nrr and nbc == nrc:   # 굴렸는데 같은 곳에 도착한 경우
        if arr[nbr][nbc] == 'O':    # 같이 구멍에 빠지는 경우
            fall_together = True
        if br < rr:
            nrr += 1
        else:
            nbr += 1
    
    if (nbr, nbc, nrr, nrc) not in visited_dic and arr[nbr][nbc] != 'O' and not fall_together:
        visited_dic[(nbr, nbc, nrr, nrc)] = visited_dic[(br, bc, rr, rc)] + 1
        rst_lst.append((nbr, nbc, nrr, nrc))
    
    # 아래쪽으로 기울이기
    nbr, nbc, nrr, nrc = br, bc, rr, rc
    fall_together = False

    while arr[nbr+1][nbc] != '#' and arr[nbr][nbc] != 'O':
        nbr += 1
    while arr[nrr+1][nrc] != '#' and arr[nrr][nrc] != 'O':
        nrr += 1
    
    if nbr == nrr and nbc == nrc:   # 굴렸는데 같은 곳에 도착한 경우
        if arr[nbr][nbc] == 'O':    # 같이 구멍에 빠지는 경우
            fall_together = True
        if br < rr:
            nbr -= 1
        else:
            nrr -= 1
    
    if (nbr, nbc, nrr, nrc) not in visited_dic and arr[nbr][nbc] != 'O' and not fall_together:
        visited_dic[(nbr, nbc, nrr, nrc)] = visited_dic[(br, bc, rr, rc)] + 1
        rst_lst.append((nbr, nbc, nrr, nrc))
        
    return rst_lst


def bfs(sbr, sbc, srr, src):
    q = deque()
    q.append((sbr, sbc, srr, src))
    visited_dic[(sbr, sbc, srr, src)] = 0
    
    while q:
        br, bc, rr, rc = q.popleft()
        rst_lst = tilt(br, bc, rr, rc)
        # print('rst_lst :', rst_lst)
        for nbr, nbc, nrr, nrc in rst_lst:
            if arr[nrr][nrc] == 'O':
                return visited_dic[(nbr, nbc, nrr, nrc)]
            q.append((nbr, nbc, nrr, nrc))
            # print('nbr, nbc, nrr, nrc, visited :', nbr, nbc, nrr, nrc, visited_dic[(nbr, nbc, nrr, nrc)])

    return -1


N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

sbr, sbc, srr, src = find_start_points()
visited_dic = {}

print(bfs(sbr, sbc, srr, src))