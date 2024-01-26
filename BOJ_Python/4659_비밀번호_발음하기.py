import sys; input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}

def evaluate(pw):
    # 모음 포함
    if len(vowels & set(pw)) == 0:
        return False

    # 모음 혹은 자음 3개 연속 X
    cnt_v = cnt_c = 0
    for a in pw:
        if a in vowels:
            cnt_v += 1  # 모음 cnt 증가
            cnt_c = 0   # 자음 cnt 초기화
        else:
            cnt_c += 1  # 자음 cnt 증가
            cnt_v = 0   # 모음 cnt 초기화
        if cnt_v >= 3 or cnt_c >= 3:
            return False

    # 같은 글자 연속 2번 x (ee와 oo는 허용)
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] not in 'eo':
            return False

    return True


while True:
    pw = input().strip()
    if pw == 'end': break

    rst = evaluate(pw)
    if rst: print(f'<{pw}> is acceptable.')
    else:   print(f'<{pw}> is not acceptable.')