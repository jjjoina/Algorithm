import sys; input = sys.stdin.readline

N = int(input())
heights = [0] * 1001
for _ in range(N):
    i, h = map(int, input().split())
    heights[i] = h

# 시작점, 끝점 찾기
start = end = 0
for i in range(1001):
    if heights[i]:
        start = i
        break
for i in range(1000, -1, -1):
    if heights[i]:
        end = i
        break

# 최대 높이인 인덱스 찾기
max_idx = start
for i in range(start+1, end+1):
    if heights[max_idx] < heights[i]: max_idx = i

# max_idx의 왼쪽
for i in range(start+1, max_idx):
    if heights[i] < heights[i-1]:
        heights[i] = heights[i-1]
# max_idx의 오른쪽
for i in range(end-1, max_idx, -1):
    if heights[i] < heights[i+1]:
        heights[i] = heights[i+1]

print(sum(heights[start:end+1]))