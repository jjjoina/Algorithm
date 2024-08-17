e = 1e-9

def is_cross():
    if x2 < x3 or x4 < x1:  # x의 범위가 겹치지 않는 경우
        return 0

    if x1 == x2:
        L1_up_y = max(y1, y2)
        L1_down_y = min(y1, y2)

        if x3 == x4:    # L1, L2 둘 다 y축과 평행한 경우
            if x1 != x3:
                return 0

            L2_up_y = max(y3, y4)
            L2_down_y = min(y3, y4)

            if L1_up_y < L2_down_y or L1_down_y > L2_up_y:
                return 0
            else:
                return 1

        else:           # L1만 y축과 평행한 경우
            L2_y = ((y4 - y3) / (x4 - x3)) * (x1 - x3) + y3

            if L2_y > L1_up_y or L2_y < L1_down_y:
                return 0
            else:
                return 1

    if x3 == x4:        # L2만 y축과 평행한 경우
        L2_up_y = max(y3, y4)
        L2_down_y = min(y3, y4)
        L1_y = ((y2 - y1) / (x2 - x1)) * (x3 - x1) + y1

        if L1_y > L2_up_y or L1_y < L2_down_y:
            return 0
        else:
            return 1

    # L1, L2 둘 다 y축과 평행하지 않은 경우
    left_x = max(x1, x3)
    right_x = min(x2, x4)

    L1_left_y = ((y2 - y1) / (x2 - x1)) * (left_x - x1) + y1
    L1_right_y = ((y2 - y1) / (x2 - x1)) * (right_x - x1) + y1
    L2_left_y = ((y4 - y3) / (x4 - x3)) * (left_x - x3) + y3
    L2_right_y = ((y4 - y3) / (x4 - x3)) * (right_x - x3) + y3

    if -e < L1_left_y - L2_left_y < e or -e < L1_right_y - L2_right_y < e:
        return 1

    if L1_left_y > L2_left_y:
        if L1_right_y < L2_right_y:
            return 1
        else:
            return 0
    else:
        if L1_right_y > L2_right_y:
            return 1
        else:
            return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if x1 > x2:     # L1의 양 끝점 x좌표 오름차순 정렬
    x1, y1, x2, y2 = x2, y2, x1, y1
if x3 > x4:     # L2의 양 끝점 x좌표 오름차순 정렬
    x3, y3, x4, y4 = x4, y4, x3, y3

print(is_cross())