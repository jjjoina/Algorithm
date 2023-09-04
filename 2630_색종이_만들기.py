import sys; input = sys.stdin.readline

def divide(paper):
    color = paper[0][0]
    n = len(paper)
    for i in range(n):
        for j in range(n):
            if paper[i][j] != color:
                # 색종이가 아니므로 4등분하여 재귀로 조사
                divs = [[] for _ in range(4)]
                for k in range(n//2):
                    divs[0].append(paper[k][:n//2])
                    divs[1].append(paper[k][n//2:])
                for k in range(n//2, n):
                    divs[2].append(paper[k][:n//2])
                    divs[3].append(paper[k][n//2:])
                for k in range(4):
                    divide(divs[k])
                return
    # 색종이임!
    ans[color] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0]
divide(arr)
for i in range(2):
    print(ans[i])