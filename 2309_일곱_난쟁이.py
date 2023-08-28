import sys; input = sys.stdin.readline

def find():
    for i in range(9):
        for j in range(i+1, 9):
            if heights[i] + heights[j] == over:
                return (i, j)


heights = [int(input()) for _ in range(9)]
heights.sort()

over = sum(heights) - 100
i, j = find()

for k in range(9):
    if k not in [i, j]:
        print(heights[k])