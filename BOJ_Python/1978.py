N = int(input())
numbers = list(map(int, input().split()))

# 에라토스테네스의 체로 1000 이하의 소수 리스트 만들기
primes = list(range(2, 1001))
idx = 0
prime = primes[idx]
while prime < 1000**0.5:
    # 소수의 배수들 제거
    multiples = [prime * i for i in range(2, 1000//prime + 1)]
    for multiple in multiples:
        if multiple in primes:
            primes.remove(multiple)
    idx += 1
    prime = primes[idx]

ans = 0
for number in numbers:
    if number in primes:
        ans += 1
print(ans)

# 두 번째 풀이
# N = int(input())
# numbers = list(map(int, input().split()))
# # 숫자 하나씩 꺼내서 작업
# # 소수면 카운트 하나 추가
# ans = 0
# for number in numbers:
#     if number > 1:
#         # 소수이기 위해서는 2~해당수**0.5까지 중에 약수가 없어야 한다.
#         for d in range(2, int(number**0.5)+1):
#             if number % d == 0:
#                 break
#         # number가 소수인 경우 실행되는 else문
#         else:
#             ans += 1
# print(ans)