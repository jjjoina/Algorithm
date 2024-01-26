import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())
for _ in range(S):
    gender, n = map(int, input().split())
    if gender == 1:     # 남자인 경우
        for i in range(n-1, N, n):  # n의 배수들에 대해
            arr[i] = 1 - arr[i]     # 스위치 변경
    elif gender == 2:   # 여자인 경우
        n -= 1          # 인덱스 조절
        d = 0
        while d <= n < N-d and arr[n-d] == arr[n+d]:
            arr[n-d] = arr[n+d] = 1 - arr[n-d]
            d += 1

i = 0
while i < N:
    if i and i % 20 == 0: print('\n', end='')
    print(arr[i], end=' ')
    i += 1