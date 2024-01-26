import sys; input = sys.stdin.readline

grade_to_point = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

arr = [input().split()[1:] for _ in range(20)]

total_point = 0
total_time = 0
for t, g in arr:
    if g == 'P': continue   # P인 경우 고려 (p면 continue)

    t = float(t)
    total_point += t * grade_to_point[g]
    total_time += t

print(total_point / total_time)