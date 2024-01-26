import sys; input = sys.stdin.readline

N, t_score, P = map(int, input().split())
# N : 리스트에 있는 점수의 개수
# P : 랭킹 리스트에 올라갈 수 있는 점수의 개수
if N:
    lst = list(map(int, input().split()))

    # 자기보다 점수 높은 사람들의 수
    ans = 1
    cnt = 0
    for score in lst:
        if t_score < score: ans += 1
        if t_score <= score: cnt += 1

    if cnt == P: print(-1)      # 랭킹 리스트의 점수들이 모두 태수 점수 이상이었을 경우
    else:        print(ans)     # 태수가 랭킹 리스트에 오른 경우 자기보다 높은 사람들의 수 + 1 출력

else:
    print(1)