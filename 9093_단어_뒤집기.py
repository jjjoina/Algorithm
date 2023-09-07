import sys; input = sys.stdin.readline

def reverse(word):
    lst = list(word)
    N = len(lst)
    for i in range(N//2):
        lst[i], lst[N-1-i] = lst[N-1-i], lst[i]
    return ''.join(lst)


T = int(input())
for t in range(1, T+1):
    s = input().split()
    for i in range(len(s)):
        s[i] = reverse(s[i])
    print(' '.join(s))