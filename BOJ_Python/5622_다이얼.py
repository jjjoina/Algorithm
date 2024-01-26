# 풀이 2. 리스트 활용
lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
ans = 0
for c in s:
    for i in range(len(lst)):
        if c in lst[i]:
            ans += i + 3
            break   # 다음 글자 진행
print(ans)


# 풀이 1.
# s = input()
# ans = 0
# for c in s:
#     if c in 'ABC': ans += 3
#     elif c in 'DEF': ans += 4
#     elif c in 'GHI': ans += 5
#     elif c in 'JKL': ans += 6
#     elif c in 'MNO': ans += 7
#     elif c in 'PQRS': ans += 8
#     elif c in 'TUV': ans += 9
#     elif c in 'WXYZ': ans += 10
# print(ans)