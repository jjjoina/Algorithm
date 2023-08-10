# 5로 최대한 나눈다
# 3도 맞아떨어질 때까지 5에서 덜고 3에서 더한다

for N in range(1, 101):

    five = N // 5

    while five >= 0 and (N - 5*five) % 3 != 0:
        five -= 1

    if five == -1:
        print(five)
    else:
        three = (N - 5*five) // 3
        print(five + three)