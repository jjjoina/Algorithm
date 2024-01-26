import sys; input = sys.stdin.readline

def perm(i, prev):
    # i번째 원소를 선택하는 함수
    if i == M:
        print(*p)
        return
    
    for j in range(prev, N):
        p.append(lst[j])
        perm(i+1, j)
        p.pop()


N, M = map(int, input().split())
lst = list(set(map(int, input().split())))  # 중복 제거
N = len(lst)

lst.sort()
p = []
perm(0, 0)