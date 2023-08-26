import sys; input = sys.stdin.readline

# 풀이 2. [더 빠름] 풀이 1과 다르게 lst가 전역변수임
def dfs(top):
    # top : lst에 마지막으로 넣은 원소
    if len(lst) == M:
        print(*lst)
        return

    for new_top in range(top+1, N+1):
        lst.append(new_top)
        dfs(new_top)
        lst.pop()


N, M = map(int, input().split())
lst = []
dfs(0)


# # 풀이 1. [더 느림] 호출되는 함수마다 개별 lst를 가짐
# def sequence(i, lst):
#     # i : 현재 고른 개수 / lst : 지금까지 고른 것들
#     if i == M:
#         print(*lst)
#         return

#     if i == 0:
#         for new in range(1, N+1):
#             sequence(i+1, lst+[new])
    
#     # i번째 원소를 골라보자
#     else:
#         for new in range(lst[-1]+1, N+1):
#             sequence(i+1, lst+[new])


# N, M = map(int, input().split())
# sequence(0, [])