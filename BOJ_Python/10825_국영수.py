import sys; input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    student = input().split()
    lst.append([student[0], int(student[1]), int(student[2]), int(student[3])])

lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in lst:
    print(student[0])