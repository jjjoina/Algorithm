import sys; input = sys.stdin.readline

for _ in range(int(input())):
    w1, w2 = input().split()
    ans = []
    for i in range(len(w1)):
        if w1[i] <= w2[i]:
            ans.append(ord(w2[i]) - ord(w1[i]))
        else:
            ans.append(ord(w2[i]) + 26 - ord(w1[i]))
            
    print('Distances:', *ans)