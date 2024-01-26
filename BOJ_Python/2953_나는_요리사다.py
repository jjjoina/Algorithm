winner = 0
max_point = 0

for i in range(1, 6):
    point = sum(map(int, input().split()))
    if max_point < point:
        max_point = point
        winner = i

print(winner, max_point)