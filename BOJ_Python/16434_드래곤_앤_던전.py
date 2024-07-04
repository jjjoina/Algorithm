import sys; input = sys.stdin.readline
import math

N, atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

# 최종 atk 구하기
for i in range(N):
    if rooms[i][0] == 2:
        atk += rooms[i][1]

cur_hp = ans = 1
for i in range(N-1, -1, -1):
    if rooms[i][0] == 1:
        cur_hp += rooms[i][1] * (math.ceil(rooms[i][2] / atk) - 1)
        if ans < cur_hp:
            ans = cur_hp
    else:
        atk -= rooms[i][1]
        cur_hp -= rooms[i][2]
        if cur_hp < 1:
            cur_hp = 1

print(ans)