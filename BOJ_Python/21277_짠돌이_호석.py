import sys; input = sys.stdin.readline

def check(n1_s, m1_s, n2_s, m2_s, h, w):
    for i in range(h):
        for j in range(w):
            if p1[n1_s+i][m1_s+j] == 1 and p2[n2_s+i][m2_s+j] == 1:
                return False

    return True


def rotate(p, r, c):    # 시계 방향으로 90도 회전
    return [[p[r-1-j][i] for j in range(r)] for i in range(c)], c, r


# def print_puzzles():    # 디버깅용
#     print('------ print_puzzles -----')
#     for i in range(N1):
#         for j in range(M1):
#             if n1_s <= i < n1_e and m1_s <= j < m1_e:
#                 print('■', end='')
#             else:
#                 print(p1[i][j], end='')
#         print()
#     print()
#     for i in range(N2):
#         for j in range(M2):
#             if n2_s <= i < n2_s+(n1_e-n1_s) and m2_s <= j < m2_s+(m1_e-m1_s):
#                 print('■', end='')
#             else:
#                 print(p2[i][j], end='')
#         print()


N1, M1 = map(int, input().split())
p1 = [list(map(int, input().strip())) for _ in range(N1)]
N2, M2 = map(int, input().split())
p2 = [list(map(int, input().strip())) for _ in range(N2)]

ans = min(
    (M1 + M2) * max(N1, N2),
    (N1 + N2) * max(M1, M2),
    (M1 + N2) * max(N1, M2),
    (N1 + M2) * max(M1, N2)
)
# print('init_ans', ans)

for r in range(4):
    for n in range(N1+N2-1):
        for m in range(M1+M2-1):
            n1_s, n1_e = max(0, n-(N2-1)), 1 + min(n, N1-1)
            m1_s, m1_e = max(0, m-(M2-1)), 1 + min(m, M1-1)

            height = N1 + N2 - (n1_e - n1_s)
            width = M1 + M2 - (m1_e - m1_s)
            area = height * width
            # print('\nr, area', r, area)

            if ans <= area:
                continue

            n2_s = (N2-1) - min(n, N2-1)
            m2_s = (M2-1) - min(m, M2-1)

            if check(n1_s, m1_s, n2_s, m2_s, n1_e-n1_s, m1_e-m1_s):
                # print_puzzles()
                ans = area
                # print('r, new_ans', r, ans)

    p2, N2, M2 = rotate(p2, N2, M2)

print(ans)