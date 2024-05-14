# 풀이 2. [40ms] datetime 안 쓰고
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

D, M = map(int, input().split())

print(day_of_the_week[(sum(days[:M]) + D) % 7])



# # 풀이 1. [68ms] datetime
# import datetime

# day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# D, M = map(int, input().split())

# print(day_of_the_week[datetime.date(2009, M, D).weekday()])