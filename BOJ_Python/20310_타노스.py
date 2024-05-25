import sys; input = sys.stdin.readline

S = list(input().strip())

cnt0 = 0
cnt1 = 0
l = 0
for c in S:
    l += 1
    if c == '0':
        cnt0 += 1
    else:
        cnt1 += 1
cnt0 //= 2
cnt1 //= 2

# 뒤쪽의 0 없애기
for i in range(l-1, -1, -1):
    if S[i] == '0':
        S[i] = ''
        cnt0 -= 1        
        if cnt0 == 0:
            break
    
# 앞쪽의 1 없애기
for i in range(l):
    if S[i] == '1':
        S[i] = ''
        cnt1 -= 1
        if cnt1 == 0:
            break
        
print(''.join(S))