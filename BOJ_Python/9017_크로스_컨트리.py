import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    # cnt[i] : i팀의 인원 수
    cnt = [0] * 201
    for i in range(1, N+1):
        cnt[lst[i]] += 1
    
    # 6명보다 적은 팀 체크하기
    is_six = [0] * 201
    for t in range(1, 201):
        if cnt[t] == 6: is_six[t] = 1        

    # 팀별 점수 리스트 생성
    points = [[] for _ in range(201)]
    point = 1
    for i in range(1, N+1):
        if is_six[lst[i]]:
            points[lst[i]].append(point)
            point += 1
    
    # 팀별 점수
    min_point = 987654321
    for t in range(1, 201):
        if points[t]:
            # 점수가 낮은 팀이 우승 or 점수가 가장 낮은 팀이 여러 개인 경우 다섯 번째 선수의 점수가 낮은 팀이 우승
            if min_point > sum(points[t][:4]) or (min_point == sum(points[t][:4]) and fifth > points[t][4]):
                min_point = sum(points[t][:4])
                fifth = points[t][4]
                ans = t

    print(ans)