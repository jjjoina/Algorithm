import sys; input = sys.stdin.readline

n = int(input())

birthdays = []
for _ in range(n):
    name, day, month, year = input().split()
    birthdays.append([int(year), int(month), int(day), name])

birthdays.sort()

print(birthdays[-1][3])
print(birthdays[0][3])