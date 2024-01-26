# 45분 알람 일찍 설정하기
h, m = map(int, input().split())
m -= 45
if m < 0:
    m += 60
    h -= 1
    h %= 24
print(h, m)