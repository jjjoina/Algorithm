# 풀이 2. (런타임 에러) 고침
import sys; input = sys.stdin.readline

n = int(input())
cnt = [0] * 31
for _ in range(n):
    cnt[int(input())] += 1

# cut : 제외할 15%
cut = int(n * 0.15 + 0.5)
# 아래 절삭
c = cut
i = 1
while c:
    tmp = min(cnt[i], c)
    cnt[i] -= tmp
    c -= tmp
    i += 1
# 위 절삭
c = cut
i = 30
while c:
    tmp = min(cnt[i], c)
    cnt[i] -= tmp
    c -= tmp
    i -= 1
# 절삭 완료

# 평균 구하기
sum_v = 0
for i in range(1, 31):
    sum_v += i * cnt[i]

if n:
    print(int(sum_v / (n - 2*cut) + 0.5))
else:
    print(0)


# 풀이 1. (런타임 에러) 고침
import sys; input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# 제외할 15%
cut = n * 0.15
# 반올림
cut = int(cut + 0.5)

if n:
    print(int(sum(arr[cut:n-cut]) / (n - 2*cut) + 0.5))
else:
    print(0)