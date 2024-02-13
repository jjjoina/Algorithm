import sys; input = sys.stdin.readline

while True:
    name, age, weight = input().split()
    if (name, age, weight) == ('#', '0', '0'): break
    age, weight = int(age), int(weight)

    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")