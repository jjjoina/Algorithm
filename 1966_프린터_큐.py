# 풀이 2. 정말 동작
import sys; input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    # N: 문서의 개수 / M : 답이 궁금한 문서의 초기 위치 (0 ~ N-1)
    N, M = map(int, input().split())
    # 중요도 리스트
    arr = list(map(int, input().split()))
    ans = 0
    # 인덱스로 이루어진 큐?
    q = list(range(N))
    while True:
        flag = 0
        for e in q:
            if arr[e] > arr[q[0]]:
                flag = 1
                break
        if flag:    # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있음
            q.append(q.pop(0))
        
        else:       # 중요도가 가장 높아서 인쇄할 수 있음
            t = q.pop(0)
            ans += 1
            if t == M: break
    
    print(ans)



# # 풀이 1. [실패]
# import sys; input = sys.stdin.readline

# T = int(input())
# for t in range(1, T+1):
#     # N: 문서의 개수 / M : 답이 궁금한 문서의 초기 위치 (0 ~ N-1)
#     N, M = map(int, input().split())
#     # 중요도 리스트
#     arr = list(map(int, input().split()))
    
#     ans = 0
#     idx = 0
#     t = arr[M]
#     for k in range(9, t, -1):
#         flag = 1
#         for i in range(N-1, -1, -1):
#             if arr[i] == k:
#                 if flag:
#                     idx = i
#                     flag = 0
#                 ans += 1
#                 arr[i] = 0

#     arr[M] = 10
#     new_arr = arr[idx:] + arr[:idx]
#     for d in new_arr:
#         if d == t: ans += 1
#         elif d == 10:
#             ans += 1
#             break
#     print(ans)