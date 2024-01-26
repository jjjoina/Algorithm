import sys; input = sys.stdin.readline
from collections import deque

def rotate_clockwise(s):
    cube[s] = [
        cube[s][6], cube[s][3], cube[s][0],
        cube[s][7], cube[s][4], cube[s][1],
        cube[s][8], cube[s][5], cube[s][2]
        ]


def rotate_counterclockwise(s):
    cube[s] = [
        cube[s][2], cube[s][5], cube[s][8],
        cube[s][1], cube[s][4], cube[s][7],
        cube[s][0], cube[s][3], cube[s][6]
        ]


def rotate_side(sides, indexes):
    buff = deque()
    
    for i in [0, 1, 2, 3]:
        for j in range(3):
            buff.append(cube[sides[i]][indexes[i][j]])

    for i in [1, 2, 3, 0]:
        for j in range(3):
            cube[sides[i]][indexes[i][j]] = buff.popleft()


for _ in range(int(input())):
    n = int(input())
    r_lst = input().split()

    cube = [[color] * 9 for color in ['w', 'y', 'r', 'o', 'g', 'b']]
    
    for r in r_lst:
        
        if r == 'U+':
            rotate_clockwise(0)
            rotate_side([2, 4, 3, 5],
                        [[2, 1, 0], [2, 1, 0], [2, 1, 0], [2, 1, 0]])

        elif r == 'U-':
            rotate_counterclockwise(0)
            rotate_side([2, 5, 3, 4],
                        [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]])

        elif r == 'D+':
            rotate_clockwise(1)
            rotate_side([2, 5, 3, 4],
                        [[6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]])

        elif r == 'D-':
            rotate_counterclockwise(1)
            rotate_side([2, 4, 3, 5],
                        [[8, 7, 6], [8, 7, 6], [8, 7, 6], [8, 7, 6]])

        elif r == 'F+':
            rotate_clockwise(2)
            rotate_side([0, 5, 1, 4],
                        [[6, 7, 8], [0, 3, 6], [2, 1, 0], [8, 5, 2]])

        elif r == 'F-':
            rotate_counterclockwise(2)
            rotate_side([0, 4, 1, 5],
                        [[8, 7, 6], [2, 5, 8], [0, 1, 2], [6, 3, 0]])

        elif r == 'B+':
            rotate_clockwise(3)
            rotate_side([0, 4, 1, 5],
                        [[2, 1, 0], [0, 3, 6], [6, 7, 8], [8, 5, 2]])
        
        elif r == 'B-':
            rotate_counterclockwise(3)
            rotate_side([0, 5, 1, 4],
                        [[0, 1, 2], [2, 5, 8], [8, 7, 6], [6, 3, 0]])
        
        elif r == 'L+':
            rotate_clockwise(4)
            rotate_side([0, 2, 1, 3],
                        [[0, 3, 6], [0, 3, 6], [0, 3, 6], [8, 5, 2]])
        
        elif r == 'L-':
            rotate_counterclockwise(4)
            rotate_side([0, 3, 1, 2],
                        [[6, 3, 0], [2, 5, 8], [6, 3, 0], [6, 3, 0]])
        
        elif r == 'R+':
            rotate_clockwise(5)
            rotate_side([0, 3, 1, 2],
                        [[8, 5, 2], [0, 3, 6], [8, 5, 2], [8, 5, 2]])
        
        elif r == 'R-':
            rotate_counterclockwise(5)
            rotate_side([0, 2, 1, 3],
                        [[2, 5, 8], [2, 5, 8], [2, 5, 8], [6, 3, 0]])
    
    print(cube[0][0] + cube[0][1] + cube[0][2])
    print(cube[0][3] + cube[0][4] + cube[0][5])
    print(cube[0][6] + cube[0][7] + cube[0][8])