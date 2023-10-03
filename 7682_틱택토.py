import sys; input = sys.stdin.readline

def game(s):
    # 개수가 이상한 경우
    if not 0 <= s.count('X') - s.count('O') <= 1:
        return 'invalid'

    # 승부
    x = is_winner(s, 'X')
    o = is_winner(s, 'O')
    if x and o: # (1) 둘 다 승리한 경우
        return 'invalid'
    elif x:     # (2) X만 승리한 경우
        if s.count('X') == s.count('O'):    # X가 승리했는데 O가 둔 경우
            return 'invalid'
    elif o:     # (3) O만 승리한 경우
        if s.count('X') > s.count('O'):     # O가 승리했는데 X가 둔 경우
            return 'invalid'
    else:       # (4) 승부가 나지 않은 경우
        if '.' in s:    # 빈칸이 있는 경우
            return 'invalid'
    
    return 'valid'


def is_winner(s, c):
    # 가로로 승리한 경우
    if s[0] == s[1] == s[2] == c or s[3] == s[4] == s[5] == c or s[6] == s[7] == s[8] == c:
        return True
    # 세로로 승리한 경우
    if s[0] == s[3] == s[6] == c or s[1] == s[4] == s[7] == c or s[2] == s[5] == s[8] == c:
        return True
    # 대각선으로 승리한 경우
    if s[0] == s[4] == s[8] == c or s[2] == s[4] == s[6] == c:
        return True
    
    return False


while True:
    tc = input().rstrip()
    if tc == 'end': break
    print(game(tc))