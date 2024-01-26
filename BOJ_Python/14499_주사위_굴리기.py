import sys; input = sys.stdin.readline

def roll(d):
    if d == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif d == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif d == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    else:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]


N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd_lst = list(map(int, input().split()))

dir = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0, 0, 0, 0, 0, 0, 0]

for cmd in cmd_lst:
    nx, ny = x+dir[cmd][0], y+dir[cmd][1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny

        roll(cmd)   # 주사위 회전

        if arr[x][y] == 0:
            arr[x][y] = dice[6]
        else:
            dice[6] = arr[x][y]
            arr[x][y] = 0
        
        print(dice[1])