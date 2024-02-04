import sys; input = sys.stdin.readline

def is_not_repeating(cnt):
    digits = [0] * 10
    
    while cnt > 0:
        d = cnt % 10
        if digits[d] == 1:
            return False
        digits[d] = 1
        cnt //= 10
    
    return True

lst = [0] * 1000001
cnt = i = 1
while i <= 1000000:
    if is_not_repeating(cnt):
        lst[i] = cnt
        i += 1
    cnt += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(lst[n])