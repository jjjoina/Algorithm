for _ in range(int(input())):
    points = [0, 0]
    
    for _ in range(9):
        y, k = map(int, input().split())
        points[0] += y
        points[1] += k

    if points[0] > points[1]:
        print('Yonsei')
    elif points[0] < points[1]:
        print('Korea')
    else:
        print('Draw')