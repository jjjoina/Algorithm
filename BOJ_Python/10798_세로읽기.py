# 다섯 개의 단어
# 세로로 읽을 때 글자가 없으면 '' 읽음
# 공백 없이 쭉~ 이어서 출력

arr = [[''] * 15 for _ in range(5)]

i = 0
for _ in range(5):
    j = 0
    for c in input():
        arr[i][j] = c
        j += 1
    i += 1

for j in range(15):
    for i in range(5):
        print(arr[i][j], end='')