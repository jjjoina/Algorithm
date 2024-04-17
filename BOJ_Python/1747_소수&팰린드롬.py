def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


# [전처리] 소수 구하기
MAX_NUM = 1003001
is_prime = [True] * (MAX_NUM + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_NUM**0.5) + 1):
    if not is_prime[i]: continue
    for m in range(2*i, MAX_NUM + 1, i):
        is_prime[m] = False

N = int(input())
while True:
    if is_palindrome(N) and is_prime[N]:
        print(N)
        break
    N += 1