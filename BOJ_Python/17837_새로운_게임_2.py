# NxN 체스판.
# 말 K개. 이동방향 정해져 있음. 쌓을 수 있음.
# 칸 색깔 : 흰0|빨1|파2
# 한 턴 : 1번 말 ~ K번 말 순차적으로 이동. 쌓여져있는 말 함께 이동.
# 말이 4개 이상 쌓이면 게임 종료
# 이동하려는 칸이
	# 흰0 : 위에 그대로 쌓음.
	# 빨1 : 위에 뒤집어 쌓음.
	# 파2 or 체스판 밖 : 이동 방향 반대가 됨. 다음 칸 확인하는데 또 파2|밖이면 stay.

import sys; input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def game():
    ans = 1
    retry = False
    while True:
        i = 0
        while i < K:
            r, c = tokens[i]
            d = directions[i]
            nr, nc = r+dr[d], c+dc[d]
            
            if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] == 2:
                if not retry:
                    directions[i] += -1 if directions[i] % 2 else 1
                    retry = True
                    continue
                
            else:
                h = heights[r][c].index(i)
                if arr[nr][nc] == 1:
                    heights[r][c][h:] = heights[r][c][h:][::-1]
                heights[nr][nc].extend(heights[r][c][h:])
                for j in heights[r][c][h:]:
                    tokens[j] = [nr, nc]
                heights[r][c] = heights[r][c][:h]
                
                if len(heights[nr][nc]) >= 4:
                    return ans
                    
            retry = False
            i += 1
        
        ans += 1
        if ans > 1000:
            return -1


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tokens = []
directions = []
heights = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    r, c, d = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    tokens.append([r, c])
    directions.append(d)
    heights[r][c].append(i)

print(game())