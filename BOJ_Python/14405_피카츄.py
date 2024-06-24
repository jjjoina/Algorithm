import sys; input = sys.stdin.readline

S = input().strip()

S = S.replace('pi', ' ')
S = S.replace('ka', ' ')
S = S.replace('chu', ' ')
S = S.strip()

print('NO' if S else 'YES')