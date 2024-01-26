# 해시 함수 : 임의의 길이 -> 고정된 길이
# 출력 : 하나의 정수
r = 31
M = 1234567891
L = int(input())
lst = list(input())
ans = 0
for i in range(L):
    ans += (ord(lst[i]) - ord('a') + 1) * r**i
print(ans % M)