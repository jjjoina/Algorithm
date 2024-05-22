import sys; input = sys.stdin.readline
import math

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

pre_sum = 0
total_pop = 0
for loc, pop in lst:
    total_pop += pop
sta = math.ceil(total_pop / 2)

for loc, pop in lst:
    pre_sum += pop
    if pre_sum >= sta:
        print(loc)
        break