import sys; input = sys.stdin.readline

keyboard_dic = {}
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
for i in range(3):
    for j in range(len(keyboard[i])):
        keyboard_dic[keyboard[i][j]] = [i, j]

for _ in range(int(input())):
    word, I = input().split()
    l = len(word)
    I = int(I)
    rst = []

    for _ in range(I):
        w = input().strip()
        dist = 0
        for i in range(l):
            dist += abs(keyboard_dic[word[i]][0] - keyboard_dic[w[i]][0]) + abs(keyboard_dic[word[i]][1] - keyboard_dic[w[i]][1])
        rst.append([w, dist])
    
    rst.sort(key=lambda x : (x[1], x[0]))

    for r in rst:
        print(*r)