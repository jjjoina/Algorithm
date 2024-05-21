def count_point(r):
    res = 0
    on_circle = 0
    for x in range(1, r):
        y = (r**2 - x**2) ** 0.5
        int_y = int(y)
        if y == int_y:
            on_circle += 1
        res += int_y
    
    # 4개의 사분면
    res *= 4
    on_circle *= 4
    
    # 4축
    res += 4 * r
    on_circle += 4
    
    # 원점
    res += 1
    
    return res, on_circle


def solution(r1, r2):
    cnt_outer, cnt_outer_on_circle = count_point(max(r1, r2))
    cnt_inner, cnt_inner_on_circle = count_point(min(r1, r2))
    answer = cnt_outer - cnt_inner + cnt_inner_on_circle
    return answer