import sys; input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

checked = [0] * (N+1)   # 역대 탐색한 곳들
ans = []
for i in range(1, N+1):
    visited = set()     # i부터 돌았을 때 거치는 곳들 (검색을 위함)
    route = []          # i부터 돌았을 때 거치는 곳들 (순서 O)
    flag = False
    v = i               # i번 정점(vertex)부터 탐색 시작
    while True:
        if checked[v]:  # 이전 for문에서 이미 탐색한 곳이면
            flag = True
            break

        route.append(v) # route에는 일단 추가

        if v in visited: break
        else: visited.add(v)

        v = arr[v]  # 다음 노드로 이동

    for w in visited: checked[w] = 1    # checked에 한번에 기록

    # flag가 True면 바로 다음 for문 진행

    if not flag:    # 이번 for문에서 최초로 찾은 loop인 경우
        end = len(route) - 1
        start = route.index(route[end])
        ans.extend(route[start:end])

ans.sort()
print(len(ans))
for v in ans:
    print(v)