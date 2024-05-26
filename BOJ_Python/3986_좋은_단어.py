import sys; input = sys.stdin.readline

def is_good_word(word):
    stack = []
    cnt_dict = {'A': 0, 'B': 0}
    
    for c in word:
        if cnt_dict[c] > 0 and stack[-1] == c:
            stack.pop()
            cnt_dict[c] -= 1
        else:
            stack.append(c)
            cnt_dict[c] += 1
    
    return stack == []


N = int(input())
ans = 0

for _ in range(N):
    word = input().strip()
    if is_good_word(word):
        ans += 1

print(ans)