import sys; input = sys.stdin.readline

def count_stars(sx, sy):
    '''
    sx, sy를 좌측 상단 꼭지점으로 하는 L*L 영역의 별의 개수를 조사
    '''
    if (sx, sy) in dic: return
    
    cnt = 0
    for star in stars:
        if 0 <= star[0] - sx <= L and 0 <= star[1] - sy <= L:
            cnt += 1
        
    dic[(sx, sy)] = cnt


N, M, L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]

dic = {}
for std in stars:       # O(K)
    for sx in range(max(0, std[0]-L), std[0]):
        sy = max(0, std[1]-L)
        count_stars(sx, sy)
    
    for sy in range(max(0, std[1]-L), std[1]):
        sx = std[0]
        count_stars(sx, sy)

    for sx in range(std[0], max(0, std[0]-L), -1):
        sy = std[1]
        count_stars(sx, sy)

    for sy in range(std[1], max(0, std[1]-L), -1):
        sx = max(0, std[0]-L)
        count_stars(sx, sy)

print(K - max(dic.values()))