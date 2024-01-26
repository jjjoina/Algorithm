import sys; input = sys.stdin.readline

def perm(i):
    # i번째 원소를 선택하는 함수
    if i == M:
        rst = tuple(p)
        if rst not in results:
            print(*rst)
            results.add(rst)
        return
    
    for j in range(N):
        if not selected[j]:
            p.append(lst[j])
            selected[j] = 1
            perm(i+1)
            p.pop()
            selected[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

p = []
selected = [0] * N
results = set()
perm(0)