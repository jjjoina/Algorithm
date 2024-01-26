import sys; input = sys.stdin.readline

N = int(input())
arr = [0] * 8001
for _ in range(N):
    n = int(input())
    arr[n] += 1

# 산술평균
# 소수점 이하 첫째 자리에서 반올림한 값
sum_v = 0
for i in range(-4000, 4001):
    sum_v += arr[i] * i
print(round(sum_v / N))

# 중앙값
cnt = 0
for i in range(-4000, 4001):
    cnt += arr[i]
    if cnt > N//2:
        print(i)
        break

# 최빈값 (mode)
# 여러 개 있을 때에는 최빈값들 중 두 번째로 작은 값
# max_cnt : 최빈값의 빈도수
max_cnt = max(arr)
flag = 0
for i in range(-4000, 4001):
    # 최빈값이 최초로 나온 경우
    if arr[i] == max_cnt and not flag:
        mode = i
        flag = 1
    # 최빈값이 두 번째로 나온 경우 mode 갱신
    elif arr[i] == max_cnt and flag:
        mode = i
        break
print(mode)

# 범위
for i in range(4000, -4001, -1):
    if arr[i]:
        max_i = i
        break
for i in range(-4000, 4001):
    if arr[i]:
        min_i = i
        break
print(max_i - min_i)